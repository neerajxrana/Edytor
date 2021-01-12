from tkinter import *
import sys
from tkinter import filedialog
import os

def nothing():
	pass

root = Tk()
root.title("Edytor")
root.geometry('700x700')
root.iconbitmap('icons/pokeball.ico')

#-------------Functions---------------------
def select_all():
	text_pad.tag_add('sel', '1.0', 'end')

def cut():
	text_pad.event_generate("<<Cut>>")
	update_line_number()

def copy():
	text_pad.event_generate("<<Copy>>")

def paste():
	text_pad.event_generate("<<Paste>>")

def undo():
	text_pad.event_generate("<<Undo>>")
	update_line_number()

def redo():
	text_pad.event_generate("<<Redo>>")
	update_line_number()

def on_find():
	t2 = Toplevel(root)
	t2.title('Find')
	t2.geometry('262x65+200+250')
	t2.transient(root)
	Label(t2, text="Find All:").grid(row=0, column=0, sticky='e')
	v = StringVar()
	e = Entry(t2, width=25, textvariable=v)
	e.grid(row=0, column=1, padx=2, pady=2, sticky='we')
	e.focus_set()
	c = IntVar()
	Checkbutton(t2, text='Ignore Case', variable=c).grid(row=1,
		column=1, sticky='e', padx=2, pady=2)
	Button(t2, text="Find All", underline=0, command=lambda:
		search_for(v.get(), c.get(), text_pad, t2, e)).grid(row=0,
		column=2, sticky='e'+'w', padx=2, pady=2)

def close_search():
	text_pad.tag_remove('match', '1.0', END)
	t2.destroy()
	t2.protocol('WM_DELETE_WINDOW', close_search)

def search_for(needle, cssnstv, text_pad, t2, e):
	text_pad.tag_remove('match', '1.0', END)
	count = 0
	if needle:
		pos = '1.0'
		while True:
			pos = text_pad.search(needle, pos, nocase=cssnstv,
				stopindex=END)
		if not pos:
			lastpos = '%s+%dc' % (pos, len(needle))
			text_pad.tag_add('match', pos, lastpos)
			count += 1
			pos = lastpos
	text_pad.tag_add('match', foreground='red',
			background='yellow')
	e.focus_set()
	t2.title('%d matches found' %count)

def open_file():
	global filename
	filename = filedialog.askopenfilename(defaultextension=".txt",
		filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	if filename == "":
		filename = None
	else:
		root.title(os.path.basename(filename) + "- Edytor")
		text_pad.delete(1.0, END)
		fh = open(filename, "r")
		text_pad.insert(1.0, fh.read())
		fh.close()
	update_line_number()

def save():
	global filename
	try:
		f = open(filename, 'w')
		letter = text_pad.get(1.0, 'end')
		f.write(letter)
		f.close()
	except:
		save_as()

def save_as():
	try:
		f = filedialog.asksaveasfilename(initialfile=
			'Untitled.txt', defaultextension=".txt",
			filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
		fh = open(f, 'w')
		textoutput = text_pad.get(1.0, END)
		fh.write(textoutput)
		fh.close()
		root.title(os.path.basename(f) + " - Edytor")
	except:
		pass

def new_file():
	root.title("Untitled")
	global filename
	filename = None
	text_pad.delete(1.0, END)
	update_line_number()

def exit_editor(event=None):
	if filedialog.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()
	root.protocol('WM_DELETE_WINDOW', exit_command)
	filemenu.add_command(label="Exit", accelerator='Alt+F4',
		command=exit_editor)

def about(event=None):
	tkMessageBox.showinfo("About", "Tkinter GUI Application by neerajxrana")

def update_line_number(event=None):
	txt = ''
	if showln.get():
		endline, endcolumn = text_pad.index('end-lc').split('.')
		txt = '\n'.join(map(str, range(1, int(endline))))
	lnlabel.config(text=txt, anchor='nw')
	currline, curcolumn = text_pad.index("insert").split('.')
	infobar.config(text='Line: %s | Column: %s' %(currline, curcolumn))
#------------------------------------------------

#-------------Menubar----------------
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
filemenu.add_command(label="Open", command=open_file, accelerator="Ctrl + O")
filemenu.add_command(label="Save", command=save, accelerator="Ctrl + S")
filemenu.add_command(label="Save As", command=save_as, accelerator="Ctrl + Shift + S")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=sys.exit, accelerator="Alt + F4")

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=undo, accelerator="Ctrl + Z")
editmenu.add_command(label="Redo", command=redo, accelerator="Ctrl + Y")
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cut, accelerator="Ctrl + X")
editmenu.add_command(label="Copy", command=copy, accelerator="Ctrl + C")
editmenu.add_command(label="Paste", command=paste, accelerator="Ctrl + V")
editmenu.add_separator()
editmenu.add_command(label="Find", underline=0, command=on_find, accelerator="Ctrl + F")
editmenu.add_command(label="Select All", command=select_all, accelerator="Ctrl + A")

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
showln = IntVar()
showln.set(1)
viewmenu.add_checkbutton(label="Show Line Number", variable=showln)
viewmenu.add_command(label="Show Info Bar at Bottom", command=nothing)
viewmenu.add_command(label="Highlight Current Line", command=nothing)
themesmenu = Menu(viewmenu, tearoff=0)
theme = IntVar()
theme.set(1)
viewmenu.add_cascade(label="Themes", menu=themesmenu)
themesmenu.add_radiobutton(label="Default White", variable=theme)


aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About", command=nothing)
aboutmenu.add_command(label="Help", command=nothing)
aboutmenu.add_command(label="Credits", command=nothing)

#----------------------------------------------------------

#-----------------Shortcut Bar----------------------
shortcutbar = Frame(root, height=25, width=500, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)

icons = ['new_file', 'open_file', 'save', 'cut', 'copy', 'paste',
	'undo', 'redo', 'on_find', 'about']
for i, icon in enumerate(icons):
	tbicon = PhotoImage(file='icons/'+icon+'.png')
	cmd = eval(icon)
	toolbar = Button(shortcutbar, image=tbicon, command=cmd)
	toolbar.image = tbicon
	toolbar.pack(side=LEFT)
shortcutbar.pack(expand=NO, fill=X)
#---------------------------------------------------


line = Frame(root, height=4, width=500, bg='green')
line.pack(expand=NO, fill=X)
lnlabel = Label(root, width=3, height=50, bg='grey')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)

text_pad = Text(root, undo=True)
text_pad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(text_pad)
text_pad.configure(yscrollcommand=scroll.set)
scroll.config(command=text_pad.yview)
scroll.pack(side=RIGHT, fill=Y)

infobar = Label(text_pad, text='Line: 1 | Column: 0')
infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')

cmenu = Menu(text_pad)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
	cmd = eval(i)
	cmenu.add_command(label=i, compound=LEFT, command=cmd)
	cmenu.add_separator()
	cmenu.add_command(label='Select All', underline=7,
		command=select_all)


root.config(menu = menubar)
root.mainloop()
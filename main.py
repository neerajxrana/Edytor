from tkinter import *
import sys

def nothing():
	pass

root = Tk()
root.title("Edytor")
root.geometry('500x500')

#-------------Menubar----------------
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=nothing, accelerator="Ctrl + N")
filemenu.add_command(label="Open", command=nothing, accelerator="Ctrl + O")
filemenu.add_command(label="Save", command=nothing, accelerator="Ctrl + S")
filemenu.add_command(label="Save As", command=nothing, accelerator="Ctrl + Shift + S")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=sys.exit, accelerator="Alt + F4")

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=nothing, accelerator="Ctrl + Z")
editmenu.add_command(label="Redo", command=nothing, accelerator="Ctrl + Y")
editmenu.add_separator()
editmenu.add_command(label="Cut", command=nothing, accelerator="Ctrl + X")
editmenu.add_command(label="Copy", command=nothing, accelerator="Ctrl + C")
editmenu.add_command(label="Paste", command=nothing, accelerator="Ctrl + V")
editmenu.add_separator()
editmenu.add_command(label="Find", command=nothing, accelerator="Ctrl + F")
editmenu.add_command(label="Select All", command=nothing, accelerator="Ctrl + A")

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Show Line Number", command=nothing)
viewmenu.add_command(label="Show Info Bar at Bottom", command=nothing)
viewmenu.add_command(label="Highlight Current Line", command=nothing)
viewmenu.add_command(label="Themes", command=nothing)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About", command=nothing)
aboutmenu.add_command(label="Help", command=nothing)
aboutmenu.add_command(label="Credits", command=nothing)

#----------------------------------------------------------


shortcutbar = Frame(root, height=25, width=500, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)
line = Frame(root, height=4, width=500, bg='green')
line.pack(expand=NO, fill=X)
lnlabel = Label(root, width=3, height=50, bg='grey')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)

text_pad = Text(root)
text_pad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(text_pad)
text_pad.configure(yscrollcommand=scroll.set)
scroll.config(command=text_pad.yview)
scroll.pack(side=RIGHT, fill=Y)

root.config(menu = menubar)
root.mainloop()

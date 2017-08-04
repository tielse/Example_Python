#!/usr/bin/env python 2.7

import Tkinter
import tkMessageBox

root=Tkinter.Tk()

def hello():
    tkMessageBox.showinfo('Question', 'Xin chao!')
bt=Tkinter.Button(root,txt='Click me!',cmd=hello())
bt.pack()
root.mainloop()
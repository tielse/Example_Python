#!/usr/bin/env python 2.7

import Tkinter
from Tkinter import *

def result():
    print 'The sum:',2+2
win=Frame()
win.pack()
Button(win,text='Add',command=result).pack(side=LEFT)
Button(win,text='Click me!').pack(side=TOP)
Button(win,text='Quit',command=win.quit).pack(side=RIGHT)
win.mainloop()
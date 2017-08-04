#!/usr/bin/env python 2.7

import Tkinter
from Tkinter import *

def result():
    print ('The sum: ',2+2)

win=Frame()
win.pack()
Label(win,text='Click Add').pack(side=TOP)
Button(win,text='Add',COMMAND=result()).pack(side=LEFT)
Button(win,text='Quit',COMMAND=win.quit()).pack(side=RIGHT)
win.mainloop()
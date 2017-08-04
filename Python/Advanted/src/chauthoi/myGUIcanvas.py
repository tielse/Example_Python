#!/usr/bin/env python 2.7

import Tkinter
from Tkinter import *

root=Tkinter.Tk()
cvas=Tkinter.Canvas(root,bg='blue',height=250,width=300)
coor=10, 50, 240, 210
arc=cvas.create_arc(coor,start=0,extent=150,f='green')
cvas.pack()
root.mainloop()
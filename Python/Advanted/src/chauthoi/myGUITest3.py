#!/usr/bin/env python 2.7

import Tkinter
from Tkinter import *
root=Tk()

Widget=Label(root)
Widget.config(text='How are you?')
Widget.pack(s=TOP,e=YES,f=BOTH)
root.mainloop()
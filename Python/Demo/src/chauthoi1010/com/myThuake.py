#!/usr/bin/env python 2.7

import sys

class Parent:
    pAttr=100
    def __init__(self):
        print 'Goi contructor lop cha'
    def pMethod(self):
        print 'Goi phuong thuc lop cha'
    def setAttr(self,attr):
        Parent.pAttr=attr
    def getAttr(self):
        print 'Thuoc tinh lop cha:',Parent.pAttr

class Child(Parent):
    def __init__(self):
        print 'Goi contructor lop con'
    def childMethod(self):
        print 'Goi phuong thuc lop con'
c=Child()
c.childMethod()
c.pMethod()
c.setAttr(150)
c.getAttr()
#!/usr/bin/env python 2.7

import sys

class Par:
    def myMethod(self):
        print 'Goi phuong thuc lop cha'
class Chi(Par):
    def myMethod(self):
        print 'Goi phuong thuc lop con'
c=Chi()
c.myMethod()
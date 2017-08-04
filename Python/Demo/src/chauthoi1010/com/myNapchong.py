#!/usr/bin/env python 2.7

import sys

class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'Vector:(%d, %d)' %(self.a,self.b)
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)
vector1=Vector(2,10)
vector2=Vector(5,9)
print vector1+vector2
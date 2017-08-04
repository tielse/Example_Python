#!/usr/bin/env python 2.7

import sys

class myclass([parentclass]):
    assignments
    def __init__(self):
        statements
    def method():
        statements
    def method2():
        statements

class animal:
    name=''
    age=0
    def __init__(self,name='',age=0):
        self.name=name
        self.age=age
    def show(self):
        print 'My name is ',self.name
    def run(self):
        print 'Animal is running...'
    def go(self):
        print 'Animal is going...'

class dog(animal):
    def run(self):
        print 'Dog is running...'

myanimal=animal()
myanimal.show()
myanimal.run()
myanimal.go()
myanimal=dog('Lucky')
myanimal.show()
myanimal.run()
myanimal.go()
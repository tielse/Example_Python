#!/usr/bin/python 2.7

import os,random,sys

list=['a','b','c','2','1']

for i in range(len(list)):
    print 'Index '+str(i)+' name: '+list[i]

del list[2]
print list
print len(list)
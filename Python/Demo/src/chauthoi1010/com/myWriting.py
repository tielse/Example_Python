#! /usr/bin/python 2.7

import sys,random,os

print 'Hello you'
str=raw_input()

print 'Hello ',str,' I think number between 1-20'
a=random.randint(1,20)

for t in range(1,7):
    print 'Take t'
    t=int(raw_input())

    if t<a:
        print 'low'
    elif t>a:
        print 'hight'
    else:
        break

if t==a:
    print 'Good job '+str+'! You are number random.'
else:
    print 'Sorry you!'
#!/usr/bin/python

import sys
import math

def main():
    n=int(input('Nhap n:'))
    s=0
    i=1
    for i in range(n):
        s+=math.pow(i+1, 2)
    print 'S(n):',s
if __name__ == '__main__':
    main()
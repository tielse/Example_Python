#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap n:'))
    s=0
    gt=1
    i=1
    if n>=0:
        for i in range(n):
            gt*=i+1
            print 'GT:',gt
            s+=gt
        print 'N!:',s
    else:
        print 'Ban nhap sai!'
if __name__ == '__main__':
    main()
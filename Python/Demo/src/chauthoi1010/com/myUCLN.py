#!/usr/bin/python

import sys

def main():
    a=int(input('Nhap a:'))
    b=int(input('Nhap b:'))
    c=1
    while (c==(a%b)!=0):
        a=b
        b=c
    print 'UCLN:',b
if __name__ == '__main__':
    main()
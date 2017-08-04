#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap so n:'))
    P=i=1
    if n>=0:
        for i in range(n):
            P=2*(i+1)+1
        print 'P(n):',P
    else:
        print 'Ban nhap sai!'
if __name__ == '__main__':
    main()
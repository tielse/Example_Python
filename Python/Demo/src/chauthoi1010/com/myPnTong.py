#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap n:'))
    P=i=1
    if n>=0:
        for i in range(n):
            P+=2*(i+1)+1
        print 'S(n):',P
    else:
        print 'No'
if __name__ == '__main__':
    main()
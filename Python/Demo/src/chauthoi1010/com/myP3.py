#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap n:'))
    tmp=i=1
    S=0
    for i in range(n):
        tmp*=i+1
        S+=tmp
    print 'S(n):',S
if __name__ == '__main__':
    main()
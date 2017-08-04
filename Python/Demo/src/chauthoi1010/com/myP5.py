#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap n:'))
    i=1
    tmp=S=0
    for i in range(n):
        tmp+=i+1
        S+=1*1.0/tmp
    print 'S(n):',S
if __name__ == '__main__':
    main()
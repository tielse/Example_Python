#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap n:'))
    i=1
    S=count=0
    for i in range(n):
        if(i%2==0):
           count+=1
    print 'Tong so chan la:',count
if __name__ == '__main__':
    main()
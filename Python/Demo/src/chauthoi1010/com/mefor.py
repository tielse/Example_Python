#!/usr/bin/python

import sys

def main():
    s=0
    n=int(input('Nhap n='))
    for i in range(0,n,+1):
        s+=i;
        print 'Output:',i
    print 'S:',s
if __name__ == '__main__':
    main()
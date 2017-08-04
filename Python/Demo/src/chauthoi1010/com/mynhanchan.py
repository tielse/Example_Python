#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap so n:'))
    if n%2==0:
        print 'So chan:',n*n
    else:
        print 'So le:',n
if __name__ == '__main__':
    main()
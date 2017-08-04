#!/usr/bin/python

import sys

def main():
    n=int(input('Nhap n:'))
    i=1
    S=0
    for i in range(n):
        S+=1*1.0/(i+1)
    print 'S(n):',S
if __name__ == '__main__':
    main()
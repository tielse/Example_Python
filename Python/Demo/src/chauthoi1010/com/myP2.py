#!/usr/bin/python

import sys
import math

def main():
    n=int(input('Nhap n:'))
    S=0
    i=1
    for i in range(n):
        S+=pow(-1, i+1)*(i+1)
    print 'S(n):',S
if __name__ == '__main__':
    main()
#!/usr/bin/env python 2.7

import os

def main():
    #arr=[1,2,3,4,5,6,7,8,9,10]
    n=int(input('Nhap so pt:'))
    print ([x for x in range(1,n+1,+1) if x%2==0])
if __name__ == '__main__':
    main()
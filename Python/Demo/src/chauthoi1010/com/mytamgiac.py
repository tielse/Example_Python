#!/usr/bin/python

import sys

def main():
    a=int(input('Nhap canh a:'))
    b=int(input('Nhap canh b:'))
    c=int(input('Nhap canh c:'))
    if a+b>c & b+c>a & c+a>b:
        print 'Tam giac deu'
    elif a==b | b==c | c==a:
        print 'Tam giac can'
    elif a*a==(b*b+c*c) | b*b==(c*c+a*a) | c*c==(a*a+b*b):
        print 'Tam giac vuong'
    else:
        print 'Tam giac thuong'
if __name__ == '__main__':
    main()
#/usr/bin/python
import __init__
import math
import sys

def pt(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print 'PTVSN'
            else:
                print 'PTVN'
        else:
            print 'x=',-c*1.0/b
    else:
        deta=math.pow(b, 2)-(4*a*c)
        if deta < 0:
            print 'PTVN'
        elif deta==0:
            print 'x1=x2=',-b*1.0/(2*a)
        else:
            print 'x1=\nx2=',(-b+math.sqrt(deta))/(2*a),(-b-math.sqrt(deta))/(2*a)
def main():
    a=int(input('Nhap so a:'))
    b=int(input('Nhap so b:'))
    c=int(input('Nhap so c:'))
    pt(a, b, c)
if __name__ == '__main__':
    main()
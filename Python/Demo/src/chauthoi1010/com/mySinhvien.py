#!/usr/bin/env python 2.7

import sys

class Sinhvien:
    count=0
    def __init__(self,ten,hocphi):
        self.ten=ten
        self.hocphi=hocphi
        Sinhvien.count+=1
    def displayCount(self):
        print 'Tong SV:%d' % Sinhvien.count
    def displaySV(self):
        print 'Ten:',self.ten,', Hoc Phi:',self.hocphi
sv1=Sinhvien('Hoang',999)
sv2=Sinhvien('Tuan',777)
sv1.displaySV()
sv2.displaySV()
print 'Tong SV:%d' %Sinhvien.count
print 'Sinhvien.__doc__',Sinhvien.__doc__
print 'Sinhvien.__name__',Sinhvien.__name__
print 'Sinhvien.__module__',Sinhvien.__module__
print 'Sinhvien.__bases__',Sinhvien.__bases__
print 'Sinhvien.__dict__',Sinhvien.__dict__
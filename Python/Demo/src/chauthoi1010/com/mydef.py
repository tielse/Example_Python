import random
import math

def myceil():
    x=1.234
    return math.ceil(x)
def myabs():
    x=-1
    return math.fabs(x)
def myfloor():
    x=1.567
    return math.floor(x)
def mymod():
    x=5
    y=4.5
    return math.fmod(x, y)
def myfexp():
    x=9
    return math.frexp(x)
def mylexp():
    x=3
    i=2
    return math.ldexp(x, i)
def mymoddf():
    x=1.45
    return math.modf(x)
def myexp():
    x=2
    return math.exp(x)
def mylog():
    x=325
    return math.log(x,2)
def mylog10():
    x=1024
    return math.log10(x)
def mypow():
    x=2
    y=3
    return math.pow(x, y)
def mysqrt():
    x=16
    return math.sqrt(x)
def myacos():
    x=90
    return math.acos(x)
def myasin():
    x=90
    return math.asin(x)
def myatan():
    x=180
    return math.atan(x)
def myatanh():
    x=180
    return math.atanh(x)
def myhypot(x,y):
    return math.hypot(x, y)
def mydegrees():
    x=34.67
    return math.degrees(x)
def myradius():
    x=90
    return math.radians(x)
def mypi():
    x=3
    return math.pi*3
def mye():
    x=2
    return float(math.e*x)
def myrandom():
    random.choice['a','s','d','h','t']
def main():
    print ('MY E:%d',mye())
    #print ('\nRandom:%s',myrandom())
if __name__ == '__main__':
    main()
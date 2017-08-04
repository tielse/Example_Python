#!/usr/bin/python

import sys

def main():
    arr={'A':1,'B':2,'C':3}
    try:
        if arr['A']>1:
            print 'True'
    except KeyError:
        print 'False'

if __name__ == '__main__':
    main()
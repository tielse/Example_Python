#!/usr/bin/env python 2.7

import sys

def main():
    arr=['a','b','c','d','e']
    result=map(lambda x:'This is %s' %x, arr)
    print result
if __name__ == '__main__':
    main()
#!/usr/bin/env python 2.7

import sys

def main():
    filter_me=[1,2,3,4,5,6,7,8,9]
    func=lambda x:x%2==0
    result=filter(func,filter_me)
    print (result)
if __name__ == '__main__':
    main()
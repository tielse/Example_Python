#!/usr/bin/env python 2.7

import os

def main():
    arr=[[2,1,1],[1,1,1],[5,5,5]]
    result=map(lambda list: [list[2],list[1],list[0]],arr)
    print result
if __name__ == '__main__':
    main()
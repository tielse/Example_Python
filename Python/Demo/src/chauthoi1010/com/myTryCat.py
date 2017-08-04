#!/usr/bin/python 2.7

import sys

def test(x):
    try:
        return 10/x
    except ZeroDivisionError:
     print('Error')

print(test(10))
print(test(0))
print(test(5))
print(test(1))
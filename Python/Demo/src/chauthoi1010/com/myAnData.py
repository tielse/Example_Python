#!/usr/bin/env python 2.7

import sys

class Just:
    count=0
    def Count(self):
        self.count+=1
        print self.count
c=Just()
c.Count()
c.Count()
print c.count
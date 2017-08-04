#!/usr/bin/env python 2.7

import os,sys

def main():
    if sys.platform=='win32':
        print 'Running on a windows platform'
        cmd='C:\\Windows\\System32\\cmd.exe'
        arr=[]
    if sys.platform=='linux32':
        print 'Running on a linux sys,identified by %s' % sys.platform
        cmd='/bin/uname'
        arr=['uname', '-a']
    print 'Running %s' % cmd
    os.spawnv(os.P_WAIT, cmd, arr)
if __name__ == '__main__':
    main()
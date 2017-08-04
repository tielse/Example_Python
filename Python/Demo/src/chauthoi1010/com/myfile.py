#!/usr/bin/env python 2.7

import sys
import os
import shutil

def make_version_path(path,version):
    if version==0:
        return path
    else:
        return path+"."+str(version)

def rotate(path,version=0):
    old_path=make_version_path(path, version)
    if not os.path.exists(old_path):
        raise IOError("'%s' khog ton tai!" % path)
    new_path=make_version_path(path, version+1)
    if os.path.exists(new_path):
        rotate(path, version+1)
    shutil.move(old_path,new_path)
def rotate_log_file(path):
    if not os.path.exists(path):
        new_file=file(path,'w')
        del new_file
    rotate(path)
def main():
    os.mkdir('C:\Users\\Administrator\\Desktop\\HakerIT')
    os.makedirs('C:\Users\\Administrator\\Desktop\\HakerIT')
    os.rmdir('C:\Users\\Administrator\\Desktop\\HakerIT')
if __name__ == '__main__':
    main()
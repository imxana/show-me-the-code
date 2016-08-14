#!/usr/bin/env python3
# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
import re

def legalname(filename):
    fn = filename.split('.')
    if fn[0] == '':
        return False
    for ln in ['c','cpp','m','js','mm','py','sh']:
        if fn[-1].lower() == ln:
            return True
    return False

def isNote(line):
    mark = ['//', '#', '\'\'\'', '\"\"\"']
    flag = False
    for m in mark:
        if line.startswith(m):
            return True
    return False

def lineCount(lines):
    code, note, blank = 0,0,0
    for line in lines:
        line = line.strip()
        if line == '':
            blank += 1
        elif isNote(line):
            note += 1
        else:
            code += 1
    return code, note, blank

if __name__ == '__main__':
    # 指明被遍历的文件夹
    rootdir =os.path.abspath(os.curdir) # +'/assets/'
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            if legalname(filename):
                infile = os.path.join(parent,filename)
                lines = open(infile, 'rU').readlines()
                print(' ',filename, ' \tcode:%d\tnote:%d\tblank:%d'%lineCount(lines))

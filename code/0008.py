#!/usr/bin/env python3
# 第 0008 题：一个HTML文件，找出里面的正文。
# 第 0009 题：一个HTML文件，找出里面的链接。
# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

import re

def count(filepath):
    f = open(filepath, 'rU')
    s = f.read()
    words = re.findall(r'[a-zA-Z0-9-]+', s)
    return len(words)

if __name__ == '__main__':
    num = count('assets/tips.txt')
    print (num)

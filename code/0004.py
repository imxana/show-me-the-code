#!/usr/bin/env python3
# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def count(filepath):
    dic = dict()
    text = open(filepath, 'rU').read()
    words = re.findall(r'[a-zA-Z0-9-’\']+', text)
    for word in words:
        word = word.lower()
        if dic.get(word, 0) == 0:
            dic[word] = 0
        dic[word] += 1
    return dic

if __name__ == '__main__':
    num = count('assets/tips.txt')
    print('Times\tWord')
    for key in num:
        print (' %d\t%s'%(num[key], key))
    print(' %d\tTotal'%len(num))

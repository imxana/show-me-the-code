#!/usr/bin/env python3
# -*-coding:utf-8-*-

''' 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights'''

output = ('Freedom', 'Human Rights')

def sensetive():
    sens = []
    lines = open('assets/filtered_words.txt').readlines()
    for line in lines:
        sens.append(line.strip())
    return sens

def repStar(word):
    s = ''
    for i in range(len(word)):
        s += '*'
    return s

if __name__ == '__main__':
    sens = sensetive()
    while True:
        t = input()
        for s in sens:
            if s in t: # contain, not equal
                t = t.replace(s, repStar(s))
        print(t)

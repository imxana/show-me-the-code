#!/usr/bin/env python3
# -*-coding:utf-8-*-

''' 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'''

output = ('Freedom', 'Human Rights')

def sensetive():
    sens = []
    lines = open('assets/filtered_words.txt').readlines()
    for line in lines:
        sens.append(line.strip())
    return sens


if __name__ == '__main__':
    sens = sensetive()
    while True:
        t = input()
        flag = 1
        for s in sens:
            if s in t: # contain, not equal
                flag = 0
        print(output[flag])

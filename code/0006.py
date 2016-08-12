#!/usr/bin/env python3
# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，
# 为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os
import re

def legalname(filename):
    fn = filename.split('.')
    return fn[0]!='' and fn[-1].lower()=='txt'


def maxWord(filepath):
    val = 0
    dic = dict()
    text = open(filepath, 'rU').read()
    words = re.findall(r'[a-zA-Z0-9-’\']+', text)
    for word in words:
        word = word.lower()
        if dic.get(word, 0) == 0:
            dic[word] = 0
        dic[word] += 1
        val = max(val, dic[word])
    words = []
    for key in dic:
        if dic[key] == val:
            words.append(key)
    return val, words


if __name__ == '__main__':
    # 指明被遍历的文件夹
    rootdir =os.path.abspath(os.curdir)+'/assets/'
    i=0
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            if legalname(filename):
                infile = os.path.join(parent,filename)
                m = maxWord(infile)
                print(filename, '%d_times_appeared: %s'%m)
                # im = Image.open(infile)   ### 此处Image.open(dir)为多数对象应用的基础.
                # im.thumbnail(size)  ### 此处size 为长度为2的tuple类型，改变图片分辨率
                # im.save(infile) ### im.save(dir)，图片处理的最后都用这个，就是保存处理过后的图片
                i+=1
                print(i, "Done")

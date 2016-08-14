#!/usr/bin/env python3

''' **第 0013 题：** 用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)
- [参考代码](http://www.v2ex.com/t/61686 "参考代码")'''

import os
import io
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image


def findImage(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup.findAll('img', class_='BDE_Image', pic_type="0")

def downloadImage(url, saveDir):
    f = urllib.request.urlopen(url)
    tmpIm = io.BytesIO(f.read())
    img = Image.open(tmpIm)
    img.save(saveDir)

if __name__ == '__main__':
    saveDir = os.path.abspath(os.curdir)+'/download/'
    imgs = findImage("http://tieba.baidu.com/p/2166231880")
    i=1
    for img in imgs:
        print(i, 'Downloading...')
        downloadImage(img['src'], '%s/%s.jpg'%(saveDir,i))
        print(i,'Done')
        i+=1

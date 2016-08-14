#!/usr/bin/env python3

'''第 0008 题：一个HTML文件，找出里面的正文。'''

import urllib.request
from bs4 import BeautifulSoup

def findBody(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup.body

if __name__ == '__main__':
    body = findBody("https://www.baidu.com")
    print(body)

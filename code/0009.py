#!/usr/bin/env python3

''' 第 0009 题：一个HTML文件，找出里面的链接。'''

import urllib.request
from bs4 import BeautifulSoup

def findHref(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup.findAll('a')

if __name__ == '__main__':
    links = findHref("http://cn.bing.com")
    for link in links:
        print(link['href'])

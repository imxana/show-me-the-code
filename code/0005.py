#!/usr/bin/env python3
# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image  ### 此处为导出包，注意字母大小写
import os, os.path

def legalname(filename):
    fn = filename.split('.')
    if fn[0] == '':
        return False
    for ln in ['jpg','jpeg','png','bmp','gif']:
        if fn[-1].lower() == ln:
            return True
    return False


if __name__ == '__main__':
    # 指明被遍历的文件夹
    rootdir =os.path.abspath(os.curdir)+'/assets/'
    size = 320, 568 ### iphone5

    i=0
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            if legalname(filename):
                #(fn[-1].lower() == 'jpg' or fn[-1].lower() == 'jpeg' or fn[-1].lower() == 'png'):
                infile=os.path.join(parent,filename)
                im = Image.open(infile)   ### 此处Image.open(dir)为多数对象应用的基础.
                im.thumbnail(size)  ### 此处size 为长度为2的tuple类型，改变图片分辨率
                im.save(infile) ### im.save(dir)，图片处理的最后都用这个，就是保存处理过后的图片
                i+=1
                print(i, "Done")

#!/usr/bin/env python3

'''第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。'''

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

def main(size):
    # 指明被遍历的文件夹
    rootdir =os.path.abspath(os.curdir)+'/assets/'
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

if __name__ == '__main__':
    size = {'4s':(320, 480), '5':(320, 568), '6':(375,667), '6p':(414,736)}
    main(size['5'])

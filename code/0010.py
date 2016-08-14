#!/usr/bin/env python3

''' 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片'''
# [阅读资料](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)

import math
import random
import string
import sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter


font_path = '/Library/Fonts/Arial.ttf'
number = 4
size = (100,30)
draw_line = True
line_number = (2,5)

def randomColor():
    r = random.randint
    return r(0, 255), r(0, 255), r(0, 255)

grey = 232 # 222
bgcolor = (grey,grey,grey)
fontcolor = randomColor() # (0,0,255)
linecolor = randomColor() # (255,0,0)


def randomR(format, *arg):
    src = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    rst = ''.join(arg)
    if len(rst) >= format:
        return rst[0:format]
    else:
        for i in range(len(rst),format):
            rst += src[random.randint(0, len(src)-1)]
            # rst += src[math.floor(random.random()*len(src))]
        return rst

def randomCode():
    width,height = size #宽和高
    image = Image.new('RGBA',(width,height),bgcolor) #创建图片
    font = ImageFont.truetype(font_path,25) #验证码的字体
    draw = ImageDraw.Draw(image)  #创建画笔
    # text = gene_text() #生成字符串
    text = randomR(number)
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / number, (height - font_height) / number),text,
            font= font,fill=fontcolor) #填充字符串
    if draw_line:
        for i in range(random.randint(line_number[0],line_number[1])):
            randomLine(draw,width,height)
    # image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    # image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    # image.save('idencode.png') #保存验证码图片
    return image

def randomLine(draw,width,height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill = linecolor)

if __name__ == '__main__':
    randomCode().show()

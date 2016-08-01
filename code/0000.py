#!/usr/bin/env python3

from PIL import Image,ImageFont,ImageDraw  #python3

def addFont(image, text, pos):
    font = ImageFont.truetype('/Library/Fonts/华文细黑.ttf',50)
    draw = ImageDraw.Draw(image)
    draw.text( pos, text, (255,0,0),font=font)
    #draw.text((0,60),unicode('你好','utf-8'),(0,0,0),font=font) 
    return image


if __name__ == '__main__':
    img = Image.open('assets/1.jpg')
    img2 = img.convert('L')
    addFont(img, u'3', (img.width*4/5,img.height*1/10)).show()

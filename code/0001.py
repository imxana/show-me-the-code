#!/usr/bin/env python3

import math, random

def randomR(format,*arg):
    src = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    rst = ''.join(arg)
    if len(rst) >= format:
        return rst[0:format]
    else:
        for i in range(len(rst),format):
            rst += src[math.floor(random.random()*len(src))]
        return rst


def create():
    rst = []
    for i in range(200):
        rst.append(randomR(30,'XANA','The','Genius'))
    return rst


if __name__ == '__main__':
    for (k,v) in enumerate(create()):
        print(k, v)
else:
    pass



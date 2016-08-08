#!/usr/bin/env python3

import math, random

if __name__ == '__main__':
    src = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(200):
        rst = '%d '%i
        for j in range(16):
            rst += src[math.floor(random.random()*len(src))]
        print(rst)

#!/usr/bin/env python3
# coding=utf-8


'''第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。'''
# 阅读资料 [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)
# 实际参考资料 http://www.qingpingshan.com/jb/python/120932.html

from cryptography.fernet import Fernet

def gene_key():
    return Fernet.generate_key()

def encrypt(text, salt):
    return Fernet(salt).encrypt(text.encode('utf-8'))

def decrypt(encrypted_text, salt):
    return str(Fernet(salt).decrypt(encrypted_text), encoding='utf-8')

if __name__ == '__main__':
    while True:
        print('Input your text:')
        text = input()
        print('Generator salt....')
        salt = gene_key()
        print('Salt: %s'%salt)
        en_text = encrypt(text, salt)
        print('Encrypted_text: %s'%en_text)
        print('Decrypting...')
        text2 = decrypt(en_text, salt)
        print('Decrypted_text: %s'%text2)
        print()

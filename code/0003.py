#!/usr/bin/env python3

'''第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。'''
# 改为MongoBD数据库

import importlib
import pymongo

# get the strs
strs = importlib.import_module('0001').create()

conn = pymongo.MongoClient('localhost',27017)
db = conn.test
# clts = db.a_code

def query():
    for code in db.a_code.find().sort("a_id", pymongo.ASCENDING):
        print(code['a_id'], code['a_code'])
    # return #.count()

def insert():
    for (i, v) in enumerate(strs):
        db.a_code.insert({'a_id':i, 'a_code': v})
    print('Successfully Saved.')

if __name__ == "__main__":
    db.a_code.remove()
    insert()
    # query()

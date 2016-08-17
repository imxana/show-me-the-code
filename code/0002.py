#!/usr/bin/env python3

'''第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。'''

import importlib
import pymysql

# get the strs
strs = importlib.import_module('0001').create()

conn = pymysql.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '',
        db = 'test',
        charset = 'utf8'
        )

cursor = conn.cursor()

def createTable():
    """Create the MySQL Table (mysql/test/a_code)"""
    init = 'CREATE TABLE a_code ('\
            'a_id INT(11) DEFAULT NULL COMMENT "activation id",'\
            'a_code VARCHAR(100) DEFAULT NULL COMMENT "activation code"'\
            ') ENGINE=INNODB DEFAULT CHARSET=utf8;'
    try:
        cursor.execute(init)
    except Exception as e:
        print('Warning: ' + str(e))
    else:
        print('Table a_code 已成功创建')


def query():
    '''query(): check if a_code Saved or not'''
    try:
        sql = "select * from a_code"
        cursor.execute(sql)
        print(cursor.fetchall())
    except Exception as e:
        print('Error: ' + str(e))


def insert():
    """insert(): insert the a_code to sql expression """
    cursor.execute('delete from a_code;') # clear the Table
    rst = 'Successfully Saved.'
    for (i, v) in enumerate(strs):
    # for i,v in strs.items():
        sql = "insert into a_code(a_id, a_code) values(%d, '%s')" % (i, v)
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print('Error: ' + str(e))
            rst = 'Save failed..'
            conn.rollback()
    print(rst)


if __name__ == "__main__":
    createTable()
    insert()
    # query()


cursor.close()
conn.close()

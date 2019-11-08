#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 09:40
# @Author  : Lqq/linqingqing
# @Site    : 
# @File    : database.py
# @Software: PyCharm

import pymysql
import traceback

class Db:

    def __init__(self,host,port,user,passwd,db,charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    # 获取连接对象
    def get_conn(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=int(self.port),
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset
            )
            return conn
        except Exception:
            traceback.print_exc()
            exit(-1)

    # 获取所有的域名
    def get_all_domain(self):
        # 获取执行工具
        conn = self.get_conn()
        cur = conn.cursor()
        list = []

        try:
            # Sql语句
            sql = "select domain as url from domain;"
            cur.execute(sql)

            # 获取该表的所有数据
            alldata = cur.fetchall()
            for s in alldata:
                list.append(s[0])

        except Exception:
            traceback.print_exc()
        finally:
            # 对该数据库操作完记得关闭
            cur.close()
            conn.close()

        return list

    # 数据库是否存在相同的域名
    def get_website(self, url):
        select_count = 0
        # 获取执行工具
        conn = self.get_conn()
        cur = conn.cursor()
        try:
            # Sql语句
            select_sql = "select * from domain where domain = {};" .format(repr(url))
            # 查看该表有多少条数据
            select_count = cur.execute(select_sql)
        except Exception:
            traceback.print_exc()
        finally:
            # 对该数据库操作完记得关闭
            cur.close()
            conn.close()
        return select_count

    # 插入域名
    def insert_domain(self, name, domain):
        # 获取执行工具
        conn = self.get_conn()
        cur = conn.cursor()

        try:

            select_sql = "select * from domain where domain = {};".format(repr(domain))
            # 查看该表有多少条数据
            select_count = cur.execute(select_sql)

            if select_count == 0:
                # Sql语句
                sql = "INSERT INTO domain (name, domain) values ({},{});".format(repr(name),repr(domain))

                cur.execute(sql)
                conn.commit()
            else:
                print("域名已经存在了！！！")
        except Exception:
            traceback.print_exc()
            conn.rollback()
        finally:
            # 对该数据库操作完记得关闭
            cur.close()
            conn.close()

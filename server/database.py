# -*- coding:utf-8 -*-
import functools
from functools import wraps
import logging

from DBUtils.PooledDB import PooledDB
import MySQLdb.cursors

db_pool: PooledDB = PooledDB(MySQLdb,
                             10,
                             host='127.0.0.1',
                             user='root',
                             passwd='root123456',
                             db='CreateSystem',
                             charset="utf8",
                             cursorclass=MySQLdb.cursors.DictCursor)


def update(pool=db_pool):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                db_connect = pool.connection()
                cursor = db_connect.cursor()
                db_connect.begin()
                rest = func(cursor, *args, **kwargs)
                db_connect.commit()
                return rest
            except Exception as e:
                db_connect.rollback()
                raise
            finally:
                cursor.close()
                db_connect.close()
        return wrapper
    return decorator


def select(pool=db_pool):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                db_connect = pool.connection()
                cursor = db_connect.cursor()
                db_connect.begin()
                return func(cursor, *args, **kwargs)
            except Exception as e:
                raise
            finally:
                db_connect.close()
                cursor.close()
        return wrapper
    return decorator

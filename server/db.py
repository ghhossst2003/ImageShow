# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app


app.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (
    'root', 'root123456', 'CreateSystem')
# 初始化数据库连接:
engine = create_engine(app.app.config['SQLALCHEMY_DATABASE_URI'])
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def instance_to_dict(inst, cls):
    d = dict()
    '''
    获取表里面的列并存到字典里面
    '''
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        d[c.name] = v
    return d

def serialize(instance, cls):
    return instance_to_dict(instance, cls)

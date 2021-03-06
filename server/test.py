# coding = utf-8

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class Image(Base):
    __tablename__ = 'cs_file'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show_name = Column(String(500), nullable=True)
    uuid_name = Column(String(50), nullable=False)
    path = Column(String(500), nullable=True)
    file_type = Column(String(10), nullable=True)


# 定义User对象:
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'user'
#
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root123456@127.0.0.1:3306/CreateSystem')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
# new_user = User(id='5', name='Bob')
new_image = Image(show_name='aaa.txt', uuid_name='fdfd.txt', path='fda', file_type='vue')
# 添加到session:
session.add(new_image)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
# print('type:', type(user))
# print('name:', user.name)
# 关闭Session:
session.close()

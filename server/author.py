# coding=utf-8

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import DBSession
from db import serialize

Base = declarative_base()


class Author(Base):
    __tablename__ = 'cs_authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)


def get_authors():
    with DBSession() as session:
        authors = session.query(Author, Author.id, Author.name).all()
    u = []
    for author in authors:
        u.append(serialize(author, Author))
    return u

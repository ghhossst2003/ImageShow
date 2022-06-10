# coding=utf-8

from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from db import DBSession
from author import Author
from image import Image
from db import serialize
from database import select
from database import db_pool

Base = declarative_base()


class ArtProduct(Base):
    __tablename__ = 'cs_art_product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, nullable=True)
    file_id = Column(Integer, nullable=False)
    description = Column(String(500), nullable=True)
    creation_time = Column(BigInteger, nullable=True)
    upload_time = Column(BigInteger, nullable=True)


def save_art_product(author, image_id, description, create_time, upload_time):
    session = DBSession()
    image = ArtProduct(author_id=author, file_id=image_id,
                       description=description, creation_time=create_time,
                       upload_time=upload_time)
    session.add(image)
    session.commit()
    session.close()


def get_works():
    with DBSession() as session:
        records = session.query(ArtProduct.id, ArtProduct.description, ArtProduct.creation_time, ArtProduct.upload_time, Image.path, Author.name).outerjoin(Image, Image.id == ArtProduct.file_id).outerjoin(Author, Author.id == ArtProduct.author_id).all()
    u = []
    for record in records:
        v = {}
        for key in record.keys():
            v[key] = record[key]
        u.append(v)
    return u


@select(db_pool)
def get_works1(cursor, *args, **kwargs) -> object:
    page = kwargs['page']
    sql = '''select art.id, art.description, art.creation_time, art.upload_time, au.name, fi.path 
                from cs_art_product as art
                JOIN cs_authors AS au ON art.author_id = au.id
                JOIN cs_file AS fi ON art.file_id = fi.id
                order by art.upload_time desc limit %d, %d
                ''' %((page-1)*5,5)
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()

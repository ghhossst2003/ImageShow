# coding=utf-8

from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from db import DBSession
from author import Author
from image import Image
from db import serialize

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
        records = session.query(ArtProduct.description, ArtProduct.creation_time, ArtProduct.upload_time, Image.path, Author.name).outerjoin(Image, Image.id == ArtProduct.file_id).outerjoin(Author, Author.id == ArtProduct.author_id).all()
    u = []
    for record in records:
        v = {}
        for key in record.keys():
            v[key] = record[key]
        u.append(v)
    return u

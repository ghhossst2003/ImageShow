# coding=utf-8

import db
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import DBSession

Base = declarative_base()


class Image(Base):
    __tablename__ = 'cs_file'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show_name = Column(String(500), nullable=True)
    uuid_name = Column(String(50), nullable=False)
    path = Column(String(500), nullable=True)
    file_type = Column(String(10), nullable=True)


def save_image(fileName, saveName, path, fileType):
    session = DBSession()
    image = Image(show_name=fileName, uuid_name=saveName,
                  path=path, file_type=fileType)
    session.add(image)
    session.flush()
    inserted_id = image.id
    session.commit()
    session.close()
    return inserted_id

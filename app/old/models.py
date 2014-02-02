from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from datetime import datetime

# declare base model class

Base = declarative_base()

# define Volume model class

class Volume(Base):
    __tablename__ = 'volume'

    id = Column(Integer, primary_key = True)
    title = Column(String(256))
    md5 = Column(String(100))
    type = Column(String(10))
    num = Column(Integer)
    added = Column(DateTime)
    viewed = Column(DateTime)
    comments = Column(Text)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Volume %r>' % self.title

# define Tag model class

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    descr = Column(String(256))

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

    def __repr__(self):
        return '<Tag %r>' % self.name

# define Image model class

class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key = True)
    volume_id = Column(Integer, ForeignKey('volume.id')) # Foreign Key field
    path = Column(String(512))
    thumb = Column(String(512))

    def __init__(self, path, thumb):
        self.path = path
        self.thumb = thumb

    def __repr__(self):
        return'<Image %r>' % self.id
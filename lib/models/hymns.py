from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .__init__ import Base, SessionLocal

class Hymn(Base):
    __tablename__ = 'hymns'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    title = Column(String, nullable=False)
    lyrics = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    key_id = Column(Integer, ForeignKey('keys.id'), nullable=False)

    author = relationship("Author", back_populates="hymns")
    key = relationship("Key", back_populates="hymns")

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    hymns = relationship("Hymn", back_populates="author")

class Key(Base):
    __tablename__ = 'keys'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    hymns = relationship("Hymn", back_populates="key")

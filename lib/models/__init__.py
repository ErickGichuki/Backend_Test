from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

hymns_db = "sqlite:///hymns.db"
engine = create_engine(hymns_db)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    from .hymns import Hymn, Author, Key
    Base.metadata.create_all(bind=engine)

#!/usr/bin/env python 3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb

if __name__ == '__main__':
    engine = create_engine('sqlite:///hymns.db')
    Session = sessionmaker(bind=engine)
    session = Session()

ipdb.set_trace()
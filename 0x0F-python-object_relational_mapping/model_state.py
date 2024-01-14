#!/usr/bin/python3

#from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
frm sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """Represents a State tabel"""

    __tablename__ = 'states'

    id = Column(Integer

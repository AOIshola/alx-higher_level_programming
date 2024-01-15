#!/usr/bin/python3
"""Models the City table in the database"""

from model_state import Base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class City(Base):
    """Represents a City table"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    states = relationship('State', back_populates='cities')

    def __repr__(self):
        return f"<City(name={self.name})>"

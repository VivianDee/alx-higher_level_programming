#!/usr/bin/python3

"""
    Contains the class definition of a State and an instance Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_base import Base
from sqlalchemy.orm import relationship


class State(Base):
    """
        The State class inherits from Base
    """
    __tablename__ = "states"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='save-update, merge, delete')

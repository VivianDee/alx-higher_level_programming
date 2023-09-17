#!/usr/bin/python3

"""
    Contains the class definition of a State and an instance Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
        The City class inherits from Base
    """
    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

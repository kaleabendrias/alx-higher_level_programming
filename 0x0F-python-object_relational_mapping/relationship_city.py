#!/usr/bin/python3
""" a python file that contains the class definition of a State"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


# map class to inherit from Base
class City(Base):
    """class state"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

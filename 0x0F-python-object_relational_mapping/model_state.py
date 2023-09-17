#!/usr/bin/python3
"""states model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class State(Base):
    """ define city class """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

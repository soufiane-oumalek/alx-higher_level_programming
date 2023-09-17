#!/usr/bin/python3
"""states model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """ define city class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

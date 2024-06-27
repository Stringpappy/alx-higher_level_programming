#!/usr/bin/python3
"""
import modules and  declare class that inherite from base, declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metaldata_det = MetaData()
Base = declarative_base(metadata=metadata_det)


class State(Base):
    """
    declaring  class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

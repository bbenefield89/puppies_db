import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    address = Column(String(250))
    city = Column(String(250))
    state = Column(String(250))
    zipCode = Column(Integer)
    website = Column(String(250))
 
class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    dob = Column(String(80))
    gender = Column(String(80))
    weight = Column(Integer)
    shelter_id = relationship(Shelter)
    picture = Column(String(250))
 

engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)

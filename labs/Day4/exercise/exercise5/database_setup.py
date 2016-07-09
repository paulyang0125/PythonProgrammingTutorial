# coding=UTF-8
#!/usr/bin/env
############################################
# database_setup.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################

# 1. configuration
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship #foreigh key relatonship
from sqlalchemy import create_engine
Base = declarative_base()

# 2. create class and table representation

class Restaurant(Base):#extends the Base class
    
    __tablename__ = 'restaurant' #table representation in database
    
    
    
    #3. mapper code - column<->py variable 
    id = Column(Integer, primary_key = True)
    name = Column(String(80),nullable = False)
    
    
    
# 2. create class and table representation  

class MenuItem(Base):
    
    __tablename__ = 'menu_item'
    
    
    #3. mapper code - column<->py variable
    name = Column(String(250),nullable = False)
    id = Column(Integer,primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id')) #look inside the restaurant table and retrive its \
    #id col whenever i ask restaurant_id 
    restaurant = relationship(Restaurant)

    
## END
engine = create_engine(r'sqlite:///restaurantmenu_orm.db')
Base.metadata.create_all(engine)

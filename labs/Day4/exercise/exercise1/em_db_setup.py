#!/usr/bin/env
############################################
# em_db_setup.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################
'''
Implement a db_setup.py by using configure/class/table/mapper we told previously 
Setup a new database called employee_orm.db
Create 2 tables – one named employee and another names Address by ORM
Create the column with the proper datatype and its foreign key relationship 
Open employee.db by DB Browser for SQLite http://sqlitebrowser.org/ to check if you created correctly 
'''

#-- configure -- 
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship #foreigh key relatonship
from sqlalchemy import create_engine
Base = declarative_base()

class Employee(Base):

    __tablename__ = 'employee'
    name = Column(String(250),nullable=False)
    id = Column(Integer,primary_key=True)
    

class Address(Base):

    __tablename__ = 'address'
    id = Column(Integer,primary_key = True)
    street = Column(String(250),nullable=False)
    zip = Column(String(5))
    employee_id = Column(Integer,ForeignKey('employee.id'))
    employee = relationship(Employee)

    
  ## END
engine = create_engine(r'sqlite:///employee_orm.db')
Base.metadata.create_all(engine)



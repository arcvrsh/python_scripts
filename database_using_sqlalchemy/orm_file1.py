import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 

"""
database schema for employee table
columns  -> emp_id   emp_name   DOB   salary
types    -> int    str           str       int
property -> pk   unique  -       -       -
"""

class Employee(Base): 

    __tablename__ = 'employees' 

    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String, unique=True)
    DOB = Column(Integer)
    salary = Column(Integer)


if __name__ == "__main__": 
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)
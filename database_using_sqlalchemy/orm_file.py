import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 

"""
database schema for book table
columns  -> id   game_name   publisher   year
types    -> int    str           str       int
property -> pk   unique  -       -       -
"""

class Game(Base): 

    __tablename__ = 'games' 

    id = Column(Integer, primary_key=True)
    game_name = Column(String, unique=True)
    publisher = Column(String)
    year = Column(Integer)


if __name__ == "__main__": 
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)
from datetime import datetime
from sqlalchemy import (Table, Column, Integer, Numeric, String, ForeignKey, PrimaryKeyConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine

def main():
    Base = declarative_base()
    
    class User(Base):
        __tablename__ = "person"
        id = Column('id', Integer, primary_key=True)
        username = Column('username', String, unique=True)
    
    engine= create_engine('sqlite:////user.db', echo=True)
    Base.metadata.create_all(bind=engine)
        
    
    
if __name__ == "__main__":main()

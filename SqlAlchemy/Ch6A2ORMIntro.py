from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (sessionmaker, relationship, backref)
from Ch6A1ORMIntro import Base
from sqlalchemy import create_engine
metadata = MetaData()
engine = create_engine('sqlite:///cookie.db', echo=True)
Base.metadata.create_all(engine)
print(engine.table_names())


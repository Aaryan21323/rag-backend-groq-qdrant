from sqlalchemy import Column, Integer, String
from app.dbase.database import Base
#the format of the docs in the database
class Documents(Base):  
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    chunk_strategy = Column(String)  
    chunks = Column(Integer)

#booking data in the database
class Booking(Base):
    __tablename__="booking"

    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    date=Column(String,nullable=False)
    time=Column(String,nullable=False)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Date

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class Users2(Base):
    __tablename__ = 'users2'
    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    last_name = Column(String(3))
    birthday = Column(Date)
    email = Column(String)
    address = Column(String(5))

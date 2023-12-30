from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    orders = relationship('Order', backref='user')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    orders = relationship('Order', backref='item')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_item = Column(Integer, ForeignKey('items.id'))
    date = Column(Date)
    status = Column(String)
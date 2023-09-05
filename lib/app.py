from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database connection
DATABASE_URI = 'sqlite:///restaurant.db' # the path to the database
engine = create_engine(DATABASE_URI, echo=True)

# base class for all the classes
Base = declarative_base()


class Customer(Base):
    __tablename__='customer'
    cus_id = Column(Integer, Sequence('cus_id_seq'), primary_key=True)
    first_name = Column(String)
    last_name  =Column ( String )

    reviews = relationship("Review", back_populates="customer")
    restaurants=relationship("Review",back_populates="customer",overlaps="reviews")

class Restaurant (Base):
    __tablename__='restaurant'
    res_id = Column(Integer, Sequence('res_id_seq'), primary_key=True)
    res_name = Column(String)
    res_price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")


class Review (Base):
    __tablename__='review'
    rev_id = Column(Integer, Sequence('rev_id_seq'), primary_key=True)
    star_rating=Column(Integer)
    cus_id = Column(Integer, ForeignKey('customer.cus_id'))
    res_id = Column(Integer, ForeignKey('restaurant.res_id'))

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")


# create session
Session = sessionmaker(bind=engine)
session = Session()


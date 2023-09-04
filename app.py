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


# creating all the tables
Base.metadata.create_all(bind=engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# one_movie = session.query(Movie).filter_by(movie_id = 1).first()
# print(one_movie.director.dir_name, '*'*40)

session.close()
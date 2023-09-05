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

    def __repr__(self):
        return f"name: {self.first_name} {self.last_name}"
    
    def cus_reviews(self):
        reviews=session.query(Review).filter_by(customer_id=self.cus_id).all()
        return reviews
    
    def cust_restaurants(self):
        reviews=session.query(Review).filter_by(customer_id=self.cus_id).all()
        return [review.restaurant for review in reviews]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        review=session.query(Review).filter_by(customer_id=self.cus_id).order_by(Review.star_rating.desc()).limit(1).first()
        return review.restaurant
    
    def add_review(self, restaurant, rating):
        new_review=Review(
            star_rating=rating,
            restaurant_id=restaurant,
            customer=self
        )
        session.add(new_review)
        session.commit()

    def delete_review(self, restaurant):
        print(f"Deleting reviews for customer_id={self.cus_id} and restaurant_id={restaurant}")
        reviews = session.query(Review).filter_by(customer_id=self.cus_id, restaurant_id=restaurant).all()

        for review in reviews:
            print(f"Deleting with id {review.cus_id}")
            session.delete(review)
        
        session.commit()

        return "reviews deleted"

class Restaurant (Base):
    __tablename__='restaurant'
    res_id = Column(Integer, Sequence('res_id_seq'), primary_key=True)
    res_name = Column(String)
    res_price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")

    def __repr__(self):
        return f"name:{self.res_name}, price:{self.res_price}"
    
    def res_customers(self):
        reviews=session.query(Review).filter_by(restaurant_id=self.res_id).all()
        return [review.customer for review in reviews]
    
    def res_reviews(self):
        reviews=session.query(Review).filter_by(restaurant_id=self.res_id).all()
        return reviews
    
    @classmethod
    def fanciest_reataurant(cls):
        restaurant = session.query(Restaurant).order_by(Restaurant.res_price.desc()).first()
        return restaurant
    
    def all_reviews(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [review.full_review() for review in reviews]


class Review (Base):
    __tablename__='review'
    rev_id = Column(Integer, Sequence('rev_id_seq'), primary_key=True)
    star_rating=Column(Integer)
    cus_id = Column(Integer, ForeignKey('customer.cus_id'))
    res_id = Column(Integer, ForeignKey('restaurant.res_id'))

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def rev_customer(self):
        return self.customer
    
    def rev_restaurant(self):
        return self.restaurant
    
    def __repr__(self):
        return f"Star rating{self.star_rating}, customer id:{self.cus_id}, restaurant id:{self.res_id}"
    
    def full_review(self):
        return f"Review for {self.restaurant.res_name} by {self.customer.full_name()}  : {self.star_rating} stars"




# create session
Session = sessionmaker(bind=engine)
session = Session()


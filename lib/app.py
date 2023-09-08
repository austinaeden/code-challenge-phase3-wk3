# Importing dependencies from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database connection
DATABASE_URI = 'sqlite:///restaurant.db'  # the path to the database
engine = create_engine(DATABASE_URI, echo=False)  # Creating a database engine with echoing enabled for debugging

# Base class for all the classes
Base = declarative_base()

# Creating the Customer table
class Customer(Base):
    __tablename__ = 'customer'
    cus_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    
    # Creating relationships with reviews and restaurants
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Review", back_populates="customer", overlaps="reviews")

    # String representation of a customer object
    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}"

    # Get all reviews for this customer
    def cus_reviews(self):
        reviews = session.query(Review).filter_by(customer_id=self.cus_id).all()
        return reviews

    # Get a list of restaurants reviewed by this customer
    def cust_restaurants(self):
        reviews = session.query(Review).filter_by(customer_id=self.cus_id).all()
        return [review.restaurant for review in reviews]

    # Get the full name of the customer
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Get the favorite restaurant of the customer
    def favorite_restaurant(self):
        review = session.query(Review).filter_by(customer_id=self.cus_id).order_by(Review.star_rating.desc()).limit(1).first()
        return review.restaurant

    # Add a new review for the customer
    def add_review(self, restaurant, rating):
        new_review = Review(
            star_rating=rating,
            restaurant=restaurant,
            customer=self
        )
        session.add(new_review)
        session.commit()

    # Delete reviews for the customer
    def delete_review(self, restaurant):
        print(f"Deleting reviews for customer_id={self.cus_id} and restaurant_id={restaurant.res_id}")
        reviews = session.query(Review).filter_by(customer_id=self.cus_id, restaurant_id=restaurant.res_id).all()
        
        for review in reviews:
            print(f"Deleting with id {review.rev_id}")
            session.delete(review)

        session.commit()
        return "Reviews deleted"

# Creating the Restaurant table
class Restaurant(Base):
    __tablename__ = 'restaurant'
    res_id = Column(Integer, primary_key=True, autoincrement=True)
    res_name = Column(String)
    res_price = Column(Integer)
    
    # Creating a relationship with reviews
    reviews = relationship("Review", back_populates="restaurant")

    # String representation of a restaurant object
    def __repr__(self):
        return f"Name: {self.res_name}, Price: {self.res_price}"

    # Get customers who reviewed this restaurant
    def res_customers(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.res_id).all()
        return [review.customer for review in reviews]

    # Get reviews for this restaurant
    def res_reviews(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.res_id).all()
        return reviews

    # Get the fanciest restaurant
    @classmethod
    def fanciest_restaurant(cls):
        restaurant = session.query(Restaurant).order_by(Restaurant.res_price.desc()).first()
        return restaurant

    # Get all reviews for this restaurant
    def all_reviews(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.res_id).all()
        return [review.full_review() for review in reviews]

# Creating the Review table
class Review(Base):
    __tablename__ = 'review'
    rev_id = Column(Integer, primary_key=True, autoincrement=True)
    star_rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customer.cus_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.res_id'))
    
    # Creating relationships with restaurants and customers
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    # String representation of a review object
    def __repr__(self):
        return f"Star rating: {self.star_rating}, Customer ID: {self.customer_id}, Restaurant ID: {self.restaurant_id}"

    # Get the customer of this review
    def rev_customer(self):
        return self.customer

    # Get the restaurant of this review
    def rev_restaurant(self):
        return self.restaurant

    # Get the full review
    def full_review(self):
        return f"Review for {self.restaurant.res_name} by {self.customer.full_name()}: {self.star_rating} stars"

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

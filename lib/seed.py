# Importing dependencies from SQLAlchemy and Faker
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import Restaurant, Review, Customer
from app import Base, engine

# Create the database tables
Base.metadata.create_all(engine)

fake = Faker()

if __name__ == '__main__':
    # Define the database connection
    engine = create_engine('sqlite:///restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Clear old data
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()
    session.commit()

    print("Seeding restaurants...")
    # Create restaurants
    restaurants = [
        Restaurant(
            res_name=fake.name(),  # Generate a random restaurant name
            res_price=random.randint(500, 2000)  # Generate a random price within the specified range
        )
        for i in range(50)
    ]

    session.add_all(restaurants)
    session.commit()

    print("Seeding customers...")
    # Create customers
    customers = [
        Customer(
            first_name=fake.first_name(),  # Generate a random first name
            last_name=fake.last_name()  # Generate a random last name
        )
        for i in range(50)
    ]

    session.add_all(customers)
    session.commit()

    print("Seeding reviews...")
    # Create reviews
    reviews = [
        Review(
            star_rating=random.randint(1, 100),  # Generate a random star rating
            customer_id=random.choice(customers).cus_id,  # Assign a random customer ID
            restaurant_id=random.choice(restaurants).res_id  # Assign a random restaurant ID
        )
        for i in range(100)
    ]

    session.add_all(reviews)
    session.commit()

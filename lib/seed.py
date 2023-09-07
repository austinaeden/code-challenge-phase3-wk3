#!/usr/bin/env python3
#importing depndancies form sql alchemy and faker and also random
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import Restaurant, Review, Customer

fake = Faker()

if __name__ == '__main__':
    #defining the database connection
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # clear old data
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()
    session.commit()

    print("Seeding restaurants...")
    #creat restaurants
    restaurants = [
        Restaurant(
            res_name =fake.title(),
            res_price=random.price(500, 2000)
        )
    for i in range(50)]

    session.add_all(restaurants)
    session.commit()

    print("Seeding customers...")
    #creating customers
    customers=[
        Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
    for i in range (50)]

    session.add_all(customers)
    session.commit()

    print("Seeding reviews...")
    #creating reviews
    reviews=[
        Review(
            star_rating=random.randint(1, 100),
            cus_id=random.choice(customers).id,
            res_id=random.choice(restaurants).id
        )
    for i in range(100)]

    session.add_all(reviews)
    session.commit()
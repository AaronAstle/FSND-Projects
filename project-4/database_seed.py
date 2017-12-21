from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///bikes.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create Initial user
User1 = User(name="admin",
             email=raw_input("Enter Email Address:"))
session.add(User1)
session.commit()

# Create first category and samples items
category1 = Category(name="Road Bikes", image_name='road_category.jpg', user_id=1)
session.add(category1)
session.commit()

item1 = Item(user_id=1,
             name="Synapse Carbon 1",
             description="Carbon Road bike built for long haul ride with comfort in mind.",
             price="3499.99",
             manufacturer="Cannondale",
             category=category1)
session.add(item1)
session.commit()

item2 = Item(user_id=1,
             name="Evo Carbon 1",
             description="Carbon Road bike built for long haul ride with comfort in mind.",
             price="4499.99",
             manufacturer="Cannondale",
             category=category1)
session.add(item2)
session.commit()

item3 = Item(user_id=1,
             name="Synapse Aluminum 1",
             description="Aluminum Road bike built for long haul ride with comfort in mind.",
             price="1499.99",
             manufacturer="Cannondale",
             category=category1)
session.add(item3)
session.commit()

# Second Category and sample item
category2 = Category(name="Mountain Bikes", image_name='mtn_category.jpg', user_id=1)
session.add(category2)
session.commit()

item4 = Item(user_id = 1,
             name = "Highball",
             description ="29'er Hardtail ready for the cross country mountain trails.",
             price="2999.99",
             manufacturer="Santa Cruz",
             category=category2)
session.add(item4)
session.commit()

item5 = Item(user_id = 1,
             name = "Nomad",
             description ="Santa Cruz Things",
             price="2299.99",
             manufacturer="Santa Cruz",
             category=category2)
session.add(item5)
session.commit()

item6 = Item(user_id = 1,
             name = "Hardrock",
             description ="Aluminum Hardtail for entry riders",
             price="299.99",
             manufacturer="Specialized",
             category=category2)
session.add(item6)
session.commit()

print "Successful Seeding of data to DB!"

from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='Rohini',
    email='rohini.s07@gmail.com'
)

session.add(user1)
session.commit()

category1 = Category(
    name='Snowboarding',
    user=user1
)

session.add(category1)
session.commit()

category2 = Category(
    name='Soccer',
    user=user1
)

session.add(category1)
session.commit()

item1 = Item(
    name='Snowboard',
    description='It is exciting board. You will feel good after driving it!',
    category=category1,
    user=user1
)

session.add(item1)
session.commit()

item2 = Item(
    name='Stick',
    description='It is an amazing stick. You will feel good after playing it!',
    category=category2,
    user=user1
)

session.add(item2)
session.commit()

item3 = Item(
    name='Goggles',
    description='It is an amazing goggles. You will feel good after using it!',
    category=category1,
    user=user1
)

session.add(item3)
session.commit()

print('Finished populating the database!')

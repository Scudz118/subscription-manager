from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class SubscriptionTable(Base): #Create a table called 'subscriptions' with columns id, name and price.
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
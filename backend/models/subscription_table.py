from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class SubscriptionTable(Base): 
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
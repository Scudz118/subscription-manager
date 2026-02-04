from database.db import engine, Base
from models.subscription_table import SubscriptionTable
from fastapi import FastAPI
from models.subscription import Subscription

app = FastAPI()
Base.metadata.create_all(bind=engine) #Look at all table models and create if missing

subscriptions = []

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/subscriptions")
def get_subscriptions():
    return subscriptions

@app.post("/subscriptions")
def add_subscription(sub: Subscription):
    subscriptions.append(sub.model_dump())
    return {"message": "Subscription added"}
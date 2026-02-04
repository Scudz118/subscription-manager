from sqlalchemy.orm import Session
from database.db import engine, Base, get_db
from models.subscription_table import SubscriptionTable
from fastapi import FastAPI, Depends
from models.subscription import Subscription

app = FastAPI()
Base.metadata.create_all(bind=engine) #Look at all table models and create if missing

subscriptions = get_db()

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/subscriptions")
def get_subscriptions(db: Session = Depends(get_db)):
    return db.query(SubscriptionTable).all() #returning real records instead of python list

@app.post("/subscriptions")
def add_subscription(sub: Subscription, db: Session = Depends(get_db)):
    new_sub = SubscriptionTable(
        name=sub.name,
        price=sub.price
    )

    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)

    return {"message": "Subscription added"}
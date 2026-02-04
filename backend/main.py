from sqlalchemy.orm import Session
from database.db import engine, Base, get_db
from models.subscription_table import SubscriptionTable
from fastapi import FastAPI, Depends
from models.subscription import Subscription, SubscriptionResponse

app = FastAPI()
Base.metadata.create_all(bind=engine) 

subscriptions = get_db()


@app.get("/")
def root():
    return {"message": "Backend running"}


@app.get("/subscriptions", response_model=list[SubscriptionResponse])
def get_subscriptions(db: Session = Depends(get_db)):
    return db.query(SubscriptionTable).all()


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


@app.delete("/subscriptions/{sub_id}")
def delete_subscription(sub_id: int, db: Session = Depends(get_db)):
    sub = db.query(SubscriptionTable).filter(SubscriptionTable.id == sub_id).first()

    if not sub:
        return {"error": "Subscription not found"}

    db.delete(sub)
    db.commit()

    return {"message": "Subscription deleted"}


@app.put("/subscriptions/{sub_id}")
def update_subscription(sub_id: int, updated: Subscription, db: Session = Depends(get_db)):
    sub = db.query(SubscriptionTable).filter(SubscriptionTable.id == sub_id).first()

    if not sub:
        return {"error": "Subscription not found"}

    sub.name = updated.name
    sub.price = updated.price

    db.commit()
    db.refresh(sub)

    return {"message": "Subscription updated"}
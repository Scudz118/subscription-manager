from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

subscriptions = []

class Subscription(BaseModel):
    name: str
    price: float

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/subscriptions") #If a get request comes to /subscriptions then run function get_subscriptions()
def get_subscriptions():
    return subscriptions

@app.post("/subscriptions")
def add_subscription(sub: Subscription):
    subscriptions.append(sub.model_dump())
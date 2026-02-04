from pydantic import BaseModel

class Subscription(BaseModel):
    name: str
    price: float

class SubscriptionResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True
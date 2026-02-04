from pydantic import BaseModel

class Subscription(BaseModel):
    name: str
    price: float
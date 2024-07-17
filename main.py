from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="App"
)

bd = [
    {"id": 1, "role": "admin", "name": "Alma"},
    {"id": 2, "role": "leader", "name": "Alex"},
    {"id": 3, "role": "user", "name": "Alan"},
]

second_bd = [
    {"id": 1, "user_id": 1, "currency": "RUB", "side": "buy", "price": 70, "amount": 2.12},
    {"id": 2, "user_id": 2, "currency": "USD", "side": "sell", "price": 80, "amount": 2.12},
]



@app.get("/users/{user_id}")
async def get_user_id(user_id: int):
    return [user for user in bd if user.get("id") == user_id]

class Trade(BaseModel):
    id: int
    user_id: int
    currency: int
    side: int
    price: float
    amount: float
@app.post("/trades")
def add_trades(trades: List[Trade]):
    second_bd.extend(trades)
    return {"status": 200, "data": second_bd}

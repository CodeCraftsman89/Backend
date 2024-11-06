from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Users")

users = [
    {"id": 1, "age": "21", "name": "bob"},
    {"id": 2, "age": "45", "name": "alex"},
    {"id": 3, "age": "16", "name": "ann"}
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in users if user.get("id") == user]


users2 = [
    {"id": 1, "age": "21", "name": "bob"},
    {"id": 2, "age": "45", "name": "alex"},
    {"id": 3, "age": "16", "name": "ann"}
]


@app.post("/user/{user.id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}



fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
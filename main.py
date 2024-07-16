from fastapi import FastAPI

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

third_bd = [
    {"id": 1, "role": "admin", "name": "Alma"},
    {"id": 2, "role": "leader", "name": "Alex"},
    {"id": 3, "role": "user", "name": "Alan"},
]

@app.get("/users/{user_id}")
async def get_user_id(user_id: int):
    return [user for user in bd if user.get("id") == user_id]

@app.get("/name_users/{user_id}")
async def get_name_id(name_id: str):
    return [user for user in bd if user.get("name") == name_id]

@app.get("/prices")
async def get_prices(limit: int = 1, offset: int = 0):
    return second_bd[offset:][:limit]
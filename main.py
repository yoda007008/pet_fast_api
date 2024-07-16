from fastapi import FastAPI

app = FastAPI(
    title="App"
)

bd = [
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

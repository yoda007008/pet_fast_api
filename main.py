from fastapi import FastAPI

app = FastAPI(
    title="App"
)

bd = [
    {"id": 1, "role": "admin", "name": "Alma"},
    {"id": 2, "role": "leader", "name": "Alex"},
    {"id": 3, "role": "user", "name": "Alan"},
]
@app.get("/users")
async def get_user_id(user_id: int):
    return {"Hello": "World"}


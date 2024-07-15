from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def hello():
    return {"Hello": "World"}


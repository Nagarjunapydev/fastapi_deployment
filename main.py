import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def sample():
    return {"message": "Hello world"}


@app.get("/users")
async def Users():
    return {"message": "User added successfully"}

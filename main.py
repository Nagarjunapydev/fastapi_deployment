import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def sample():
    return {"message": "Hello world"}


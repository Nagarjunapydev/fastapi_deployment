import uvicorn
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def sample():
    return {"message": "Hello world"}


@app.get("/users")
async def Users():
    return {"message": "User added successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)

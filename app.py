from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from greeting import gen_tweet
from typing import List
import uvicorn
import os
from services.health_service import HealthService
import requests
import asyncio

# const app = express()
app = FastAPI()

usersDB = {}

health_service = HealthService()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(health_service.keep_alive())


class USER(BaseModel):
    name : str
    age : int

class TWEET(BaseModel):
    tasks : List[str]

@app.get("/api/health")
async def health_check():
    """
    Health check endpoint that returns the application status
    """
    return await health_service.health_check()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.post("/register")
def reg_user(user: USER):
    usersDB[user.name] = user.age
    return {"message": "hello", "data": user.dict()}

@app.post("/gen-tweet")
def get_tweet(data: TWEET): 
    return {"tweet" : gen_tweet(data)}
    

if __name__ == "__main__":
    # Get port from environment variable or use a default
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)

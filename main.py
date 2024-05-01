import os
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient


class User(BaseModel):
    username: str
    email: str
    password: str


class BasicResponse(BaseModel):
    message: str
    status: bool
    data: list[dict] | dict[str, str] = None


app = FastAPI()
client = AsyncIOMotorClient(os.getenv('MONGO_URI'))
db = client.AuthModule


@app.get('/', status_code=status.HTTP_200_OK)
async def root() -> BasicResponse:
    """The root endpoint"""
    
    return {
        'message': 'Authentication module v1',
        'status': True
    }


@app.post('/auth/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: User) -> BasicResponse:
    """Create a new user"""
    username_taken = await db.Users.find_one({'username': user.username})
    if username_taken:
        raise HTTPException(
            status_code=409,
            detail='The username is taken'
        )
    
    email_taken = await db.Users.find_one({'email': user.email})
    if email_taken:
        raise HTTPException(
            status_code=409,
            detail='The email is registered to another user'
        )
    
    await db.Users.insert_one(dict(user))
    return {
        'message': 'New user signup successful',
        'status': True
    }


@app.post('/auth/login', status_code=status.HTTP_200_OK)
async def login() -> BasicResponse:
    """Login with the credentials of an already signed up user"""
    return {
        'message': 'User login successful',
        'status': True
    }


@app.get('/protected', status_code=status.HTTP_200_OK)
async def protected(qparam: str = "") -> BasicResponse:
    """Protected route only accessible to loged in users"""
    
    return {
        'message': 'User authorized to access protected route',
        'status': True,
        'query-param': qparam
    }
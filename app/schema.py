from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional
class PostBase(BaseModel):
    title: str
    content: str 
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut  # Forward declaration of UserOut
    
    class Config:
        orm_mode = True
        # Allows the model to be used with ORM objects
        # and not just with dictionaries

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
        

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    # This is the id of the user that is logged in
    # and not the id of the token

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    # dir: conint(le=1) # This is a constraint that limits the value of dir to 1 or 0
    # This is used to limit the value of dir to 1 or 0
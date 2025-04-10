from pydantic import BaseModel
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str

class UserRole(str, Enum):
    READER = "reader"
    AUTHOR = "author"

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.READER

class User(UserBase):
    id: int

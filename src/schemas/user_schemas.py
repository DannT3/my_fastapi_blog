from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    id: int

class UserCreate(UserBase):
    id: int
    name: str
    age: int
    password: str
    email: str

class UserRead(UserBase):
    id: int
    name: str
    age: int

class UserUpdate(UserBase):
    name: str
    password: str = hash()
    email: str







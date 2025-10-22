from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    id: int

class UserCreate(UserBase):
    name: str
    age: int
    password: str
    email: str

class UserRead(UserBase):
    name: str
    age: int

class UserUpdate(UserBase):
    name: str
    password: str
    email: str







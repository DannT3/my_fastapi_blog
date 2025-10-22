from pydantic import BaseModel
from typing import List, Any
from datetime import datetime

class PostBase(BaseModel):
    id: int

class PostCreate(PostBase):
    title: str
    content: List[Any]
    created_at: datetime
    author_id: int

class PostResponse(PostBase):
    title: str
    content: str
    created_at: datetime

class PostUpdate(PostBase):
    title: str
    content: str


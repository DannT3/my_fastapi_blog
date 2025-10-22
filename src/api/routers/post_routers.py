from fastapi import APIRouter, Body
from src.schemas.user_schemas import UserRead
from src.schemas.post_schemas import PostCreate
from typing import List


router = APIRouter(prefix="/posts")

@router.get("/posts")
def read_posts(post: PostCreate = Body()):
    return [post.title, post.content, post.created_at, post.author_id]




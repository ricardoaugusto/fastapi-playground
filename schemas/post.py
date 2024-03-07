from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated


# Remove the direct import of UserPostResponse
# from schemas.user import UserPostResponse


class Post(BaseModel):
    # to be used in UserResponse
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: Annotated[str, StringConstraints(min_length=100, max_length=300)]
    created_at: datetime
    user_id: int


# Import UserPostResponse locally where it's used
class PostResponse(BaseModel):
    title: str
    content: str
    created_at: datetime
    user: UserPostResponse  # Use quotes for forward reference


class UserPostResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

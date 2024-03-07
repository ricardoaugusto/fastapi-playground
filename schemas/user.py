from __future__ import annotations

from typing import List

from pydantic import BaseModel

from schemas.post import PostResponse


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    name: str
    email: str
    posts: List[PostResponse] = []

    class Config:
        from_attributes = True


class UserPostResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

from datetime import datetime
from typing import Type

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbPost
from schemas.post import PostBase


def create_post(db: Session, request: PostBase) -> DbPost:
    new_post = DbPost(
        title=request.title,
        content=request.content,
        user_id=request.user_id,
        created_at=datetime.now(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_posts(db: Session) -> list[Type[DbPost]]:
    posts = db.query(DbPost).all()
    return posts


def get_post(db: Session, post_id: int) -> DbPost:
    post = db.query(DbPost).filter(DbPost.id == post_id).first()
    # if not post:
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found",
        )
    return post

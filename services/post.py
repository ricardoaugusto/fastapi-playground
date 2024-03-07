from sqlalchemy.orm.session import Session
from db.models import DbPost
from schemas.post import PostBase
from datetime import datetime


def create_post(db: Session, request: PostBase) -> DbPost:
    new_post = DbPost(
        title=request.title,
        content=request.content,
        user_id=request.user_id,
        created_at=datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_post(db: Session, post_id: int) -> DbPost:
    post = db.query(DbPost).filter(DbPost.id == post_id).first()
    return post
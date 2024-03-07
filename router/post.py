from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.post import PostResponse, PostBase
from services.post import create_post, get_post, get_posts

router = APIRouter(prefix="/post", tags=["post"])


@router.post("/", response_model=PostResponse)
def create(post: PostBase, db: Session = Depends(get_db)):
    return create_post(db, post)


@router.get("/all", response_model=List[PostResponse])
def get_all(db: Session = Depends(get_db)):
    return get_posts(db)


@router.get("/{id}", response_model=PostResponse)
def get(id: int, db: Session = Depends(get_db)):
    return get_post(db, id)

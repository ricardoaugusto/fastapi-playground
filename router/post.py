from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.post import PostResponse, PostBase
from services.post import create_post, get_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('/', response_model=PostResponse)
def create(post: PostBase, db: Session = Depends(get_db)):
    return create_post(db, post)


@router.get('/{id}', response_model=PostResponse)
def get(id: int, db: Session = Depends(get_db)):
    return get_post(db, id)

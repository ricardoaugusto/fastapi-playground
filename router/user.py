from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.user import UserBase, UserResponse
from services import user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create user
@router.post('/', response_model=UserResponse)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return user.create_user(db, request)


@router.get('/', response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user.get_users(db)


@router.get('/{id}', response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(db, id)


@router.put('/{id}')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return user.update_user(db, id, request)


@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.delete_user(db, id)

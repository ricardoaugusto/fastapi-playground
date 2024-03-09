from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.hash import Hash
from db.models import DbUser
from schemas.user import UserBase

"""
User service handles the creation of a new user in the database.
"""


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    return user


def get_user_by_email(db: Session, email: str):
    user = db.query(DbUser).filter(DbUser.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email {email} not found",
        )
    return user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update(
        {
            DbUser.name: request.name,
            DbUser.email: request.email,
            DbUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    return "ok"


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return "ok"

from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas.user import UserBase
from db.models import DbUser

"""
User service handles the creation of a new user in the database.
"""


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
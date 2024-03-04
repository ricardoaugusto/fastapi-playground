from pydantic import BaseModel

"""
Pydantic models are used for data validation and serialization,
particularly in the context of API input and output, whereas
SQLAlchemy models are typically used for defining the
structure of database tables.
"""


class UserBase(BaseModel):
    """
    Base User class
    """
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    """
    User that is returned in response
    """
    username: str
    email: str

    class Config():
        from_attributes = True

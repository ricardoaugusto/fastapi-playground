from pydantic import BaseModel


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

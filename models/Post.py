import datetime

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    author: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime

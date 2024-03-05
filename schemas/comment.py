from typing import List
from pydantic import BaseModel, Field, constr

"""
Pydantic models are used for data validation and serialization,
particularly in the context of API input and output, whereas
SQLAlchemy models are typically used for defining the
structure of database tables.
"""


class CreateCommentRequest(BaseModel):
    id: int = Field(..., title='Post ID', description='The ID of the post to comment on')
    comment: constr(min_length=100, max_length=300, pattern=r'^[a-z\s]*$') = Field(
        ..., description='The content of the comment'
    )
    v: List[str] = []

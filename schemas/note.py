from typing import List
from pydantic import BaseModel, Field, constr

"""
Pydantic models are used for data validation and serialization,
particularly in the context of API input and output, whereas
SQLAlchemy models are typically used for defining the
structure of database tables.
"""


class Note(BaseModel):
    title: str
    description: str
    user_id: int

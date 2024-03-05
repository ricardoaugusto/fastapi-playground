from pydantic import BaseModel

"""
Pydantic models are used for data validation and serialization,
particularly in the context of API input and output, whereas
SQLAlchemy models are typically used for defining the
structure of database tables.
"""


class Image(BaseModel):
    url: str
    alias: str

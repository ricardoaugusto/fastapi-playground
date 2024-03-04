import datetime

from typing import Optional, List, Dict
from pydantic import BaseModel

from schemas.image import Image as ImageModel


"""
Pydantic models are used for data validation and serialization,
particularly in the context of API input and output, whereas
SQLAlchemy models are typically used for defining the
structure of database tables.
"""

class Post(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str] = []
    meta: Dict[str, str] = {}
    image: Optional[ImageModel] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime

import datetime

from typing import Optional, List, Dict
from pydantic import BaseModel

from models.Image import Image as ImageModel

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

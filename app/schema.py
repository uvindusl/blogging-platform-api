from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    category: str
    tags: set
    created_at: datetime
    updated_at: datetime

class PostCreate(PostBase):
    pass

class Post(PostBase):
    pass

    class Config:
        orm_mode: True
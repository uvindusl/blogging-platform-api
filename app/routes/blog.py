from fastapi import FastAPI, APIRouter, Depends
from .. import models, schema
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# method to get all post
@router.get("/", response_model=List[schema.Post])
def get_blog_posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


# method to create posts
# @router.post()
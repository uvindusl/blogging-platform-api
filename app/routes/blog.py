from fastapi import FastAPI, APIRouter, Depends
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# method to get all post
@router.get("/")
def get_blog_posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


# method to create posts
# @router.post()
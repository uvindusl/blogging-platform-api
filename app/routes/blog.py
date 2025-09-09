from fastapi import FastAPI, APIRouter, Depends, status, HTTPException, Response
from .. import models, schema
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

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
@router.post('/',response_model=schema.Post, status_code=status.HTTP_201_CREATED)
def create_posts(post: schema.PostCreate, db:Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

# method to get only one post
@router.get('/{id}',response_model=schema.Post)
def get_one_post(id: int,db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    
    return post
        
# method to delete a post
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id: {id} not found')

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# method to update a post
@router.put('/{id}', response_model=schema.Post)
def update_post(id: int, update_post: schema.PostCreate, db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id: {id} not found')
   
    updated_field = update_post.dict()

    updated_field['updated_at'] = datetime.now()

    post_query.update(updated_field, synchronize_session=False)
    db.commit()
    return post_query.first()

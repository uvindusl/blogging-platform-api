from fastapi import FastAPI, APIRouter


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# dict to test 
posts = [
    {"id": 1, "title": "fisrt post", "content" : "hi everyone", "category" : "Blog", "tags" : ["blogs", "ig"]},
    {"id": 2,"title": "second post", "content" : "hi everyone2", "category" : "Sport", "tags" : ["match", "cricket"]}
]

# method to get all post
@router.get("/")
def get_blog_posts():
    return posts


# method to create posts
# @router.post()
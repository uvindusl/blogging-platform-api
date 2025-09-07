from fastapi import FastAPI

from .routes import blog
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Blogging-API!!!!!"}
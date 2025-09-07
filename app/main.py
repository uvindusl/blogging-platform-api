from fastapi import FastAPI

from .routes import blog

app = FastAPI()


app.include_router(blog.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Blogging-API!!!!!"}
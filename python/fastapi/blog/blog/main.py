from fastapi import FastAPI
from .database import engine, Base
from .routers import blog, user, auth


app = FastAPI()  # openapi_tags=tags_metadata

Base.metadata.create_all(bind=engine)  # migrate

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

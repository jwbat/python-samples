from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas


def retrieve_all(db: Session):
    return db.query(models.Blog).all()


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title = request.title,
                           body = request.body,
                           user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session):
    blog = db.query(models.Blog)\
             .filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404)
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404)
    blog.update(request.dict())
    db.commit()
    return 'updated'


def retrieve(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404,
                            detail=f'blog with id {id} is not available')
    return blog





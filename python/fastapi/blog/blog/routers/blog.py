from typing import List
from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from ..query import blog


router = APIRouter(
    prefix = '/blog',
    tags = ['Blogs'],
)
get_db = database.get_db;


@router.get('/', response_model=List[schemas.ShowBlog])
def retieve_all(db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.retrieve_all(db)


@router.post('/', status_code=201)
def create(request: schemas.Blog,
           db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=204)
def delete(id: int,
           db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=202)
def update(id: int,
           request: schemas.Blog,
           db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def retrieve(id: int,
             db: Session = Depends(get_db),
             current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.retrieve(id, db)




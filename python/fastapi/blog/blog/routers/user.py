from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..query import user


router = APIRouter(
    prefix = '/user',
    tags = ['Users'],
)
get_db = database.get_db;



@router.post('/', response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def retrieve(id: int, db: Session = Depends(get_db)):
    return user.retrieve(id, db)


@router.delete('/{id}', status_code=204)
def delete(id: int, db: Session = Depends(get_db)):
    return user.delete(id, db)


from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(name = request.name,
                           email = request.email,
                           password = Hash.encrypt(request.password))       # encrypt
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def retrieve(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404,
                            detail=f'user with id {id} is not available')
    return user


def delete(id: int, db: Session):
    user = db.query(models.User)\
             .filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=404)
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'

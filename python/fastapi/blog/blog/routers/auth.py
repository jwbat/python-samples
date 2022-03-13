from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..hashing import Hash


router = APIRouter(
    prefix = '/login',
    tags = ['Auth'],
)
get_db = database.get_db;


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user or not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=404, detail='invalid credentials')

    # generate a JWT token and return it
    access_token = token.create_access_token(data = { "sub": user.email },)
    return { "access_token": access_token, "token_type": "bearer" }


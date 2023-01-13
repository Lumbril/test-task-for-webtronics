from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import schemas, crud
from database.database import get_db
from database.schemas import Token
from services import authenticate_user
from services.token import create_access_token
from settings import ACCESS_TOKEN_EXPIRE_MINUTES

login_api = APIRouter()


@login_api.post('/login', response_model=Token)
def login(data: schemas.UserLoginSchema, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.email, data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {'access_token': access_token, 'token_type': 'bearer'}

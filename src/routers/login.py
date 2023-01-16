from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.database import get_db
from database.schemas import TokenSchema
from services import authenticate_user
from services.token import create_access_token
from settings import ACCESS_TOKEN_EXPIRE_MINUTES


login_api = APIRouter(tags=['Login'])


@login_api.post('/login', response_model=TokenSchema)
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, data.username, data.password)

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

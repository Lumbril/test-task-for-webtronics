from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import schemas, crud
from database.database import get_db
from database.schemas import Token
from services import authenticate_user

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

    return {'access_token': '1231w', 'token_type': 'bearer'}

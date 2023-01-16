from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import schemas, crud
from database.database import get_db
from database.schemas import UserSchema
from services import get_password_hash


registration_api = APIRouter(tags=['Registration'])


@registration_api.post('/registration', response_model=UserSchema)
def create_user(user: schemas.UserCreateSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user.password = get_password_hash(user.password)

    return crud.create_user(db=db, user=user)

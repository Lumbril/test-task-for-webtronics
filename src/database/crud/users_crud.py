from sqlalchemy.orm import Session

from database import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.UserModel).filter(models.UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.UserModel).filter(models.UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreateSchema):
    db_user = models.UserModel(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

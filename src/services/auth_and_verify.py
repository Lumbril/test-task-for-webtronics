from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database.crud import get_user_by_email

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user

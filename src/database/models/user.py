from sqlalchemy import Column, Integer, String, Boolean

from database.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True)
    password = Column(String(100), )
    is_active = Column(Boolean, default=True)

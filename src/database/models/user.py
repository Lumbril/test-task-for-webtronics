from sqlalchemy import Column, Integer, String, Boolean

from database.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String, )
    is_active = Column(Boolean, default=True)

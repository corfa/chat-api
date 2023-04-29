from sqlalchemy import Column, Integer, String

from db.models.base import BaseModel


class DBUsers(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
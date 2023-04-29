from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db.models import BaseModel


class Chat(BaseModel):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    messages = relationship("Message", back_populates="chat")
    users = relationship("DBUsers", secondary="chat_users")

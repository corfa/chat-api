from sqlalchemy import Column, Integer, ForeignKey

from db.models import BaseModel


class ChatUser(BaseModel):
    __tablename__ = "chat_users"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    chat_id = Column(Integer, ForeignKey("chats.id"), primary_key=True)
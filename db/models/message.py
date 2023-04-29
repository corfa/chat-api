from datetime import datetime

from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db.models import BaseModel


class Message(BaseModel):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_id = Column(Integer, ForeignKey("chats.id"))
    user = relationship("DBUsers")
    chat = relationship("Chat", back_populates="messages")

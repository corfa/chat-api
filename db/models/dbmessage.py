from datetime import datetime

from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, BOOLEAN
from sqlalchemy.orm import relationship

from db.models import BaseModel


class DBMessage(BaseModel):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_id = Column(Integer, ForeignKey("chats.id"))
    is_delete = Column(BOOLEAN)
    user = relationship("DBUsers")
    chat = relationship("DBChat", back_populates="messages")

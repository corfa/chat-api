from sqlalchemy import Column, String, Integer,BOOLEAN
from sqlalchemy.orm import relationship

from db.models import BaseModel


class DBChat(BaseModel):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_delete = Column(BOOLEAN)
    messages = relationship("DBMessage", back_populates="chat")
    users = relationship("DBUsers", secondary="chat_users")

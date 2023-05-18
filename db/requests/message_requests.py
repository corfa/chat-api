from sqlalchemy.orm import Session

from db.models import DBMessage
from shemas.message import Message


def create_message(db: Session, message: Message) -> DBMessage:
    db_message = DBMessage(text=message.text, user_id=message.user_id, chat_id=message.chat_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

from sqlalchemy.orm import Session

from db.models import DBMessage
from shemas.reqmessage import SaveMessage


def create_message(db: Session, message: SaveMessage) -> DBMessage:
    db_message = DBMessage(text=message.text, user_id=message.user_id, chat_id=message.chat_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_all_messages_for_chat(db: Session, chat_id: int):
    return db.query(DBMessage).filter(DBMessage.chat_id == chat_id).all()

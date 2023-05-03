from sqlalchemy.orm import Session

from db.models import DBChat, DBMessage
from shemas.chat import Chat


def create_chat(db: Session, chat: Chat) -> int:
    chat_db = DBChat(name=chat.name)
    db.add(chat_db)
    db.commit()
    db.refresh(chat_db)
    return chat_db.id


def get_all_chats(db: Session) -> list[type[DBChat]]:
    return db.query(DBChat).all()


def soft_del_chat(db: Session, id_: int) -> int:
    db_chat = db.query(DBChat).filter(DBChat.id == id_).first()
    db_chat.is_delete = True
    db.commit()
    return db_chat.id


def get_chat_messages(db: Session, id_: int):
    all_messages = db.query(DBMessage).filter(DBMessage.chat_id == id_).all()
    return all_messages

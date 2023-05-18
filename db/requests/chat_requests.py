from sqlalchemy.orm import Session

from db.models import DBChat, DBMessage, ChatUser
from shemas.chat import Chat


def create_chat(db: Session, user_id: int, chat: Chat) -> int:
    chat_db = DBChat(name=chat.name)
    db.add(chat_db)
    db.commit()
    db.refresh(chat_db)
    add_users_in_chat(chat_id=chat_db.id, user_id=user_id, db=db)
    return chat_db.id


def add_users_in_chat(chat_id: int, user_id: int, db: Session) -> int:
    chat_user_db = ChatUser(user_id=user_id, chat_id=chat_id)
    db.add(chat_user_db)
    db.commit()
    db.refresh(chat_user_db)
    return chat_user_db.id


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


def get_all_user_chats(db: Session, user_id: int):
    chat_user_ids = db.query(ChatUser.chat_id).filter(ChatUser.user_id == user_id).all()
    chat_ids = [chat_id for chat_id, in chat_user_ids]
    all_user_chats = db.query(DBChat).filter(DBChat.id.in_(chat_ids)).all()
    return all_user_chats


def get_chat_ids_for_user(db: Session, user_id: int):
    chat_user_ids = db.query(ChatUser.chat_id).filter(ChatUser.user_id == user_id).all()
    chat_ids = [chat_id for chat_id, in chat_user_ids]
    return chat_ids

from typing import List, Type

from sqlalchemy.orm import Session

from db.models import DBUsers
from db.requests.exception import DBUserNotFoundException
from shemas.update_user import UpdateUser
from shemas.user import User


def create_user(db: Session, user: User) -> int:
    user_db = DBUsers(username=user.username, password=user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db.id


def update_username(db: Session, id_: int, update_user: UpdateUser) -> int:
    user = db.query(DBUsers).filter(DBUsers.id == id_).first()
    user.username = update_user.username
    db.commit()
    return user.id


def get_all_users(db: Session) -> list[Type[DBUsers]]:
    return db.query(DBUsers).all()


def get_user_on_id(db: Session, id_: int) -> DBUsers:
    return db.query(DBUsers).filter(DBUsers.id == id_).first()


def get_user_on_login(db: Session, login: str) -> DBUsers:
    result = db.query(DBUsers).filter(DBUsers.username == login).first()
    if result is None:
        raise DBUserNotFoundException
    return result


def soft_del_user(db: Session, id_: int) -> int:
    db_user = db.query(DBUsers).filter(DBUsers.id == id_).first()
    db_user.is_delete = True
    db.commit()
    return db_user.id

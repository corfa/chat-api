from typing import Type

from sqlalchemy.orm import Session

from db.models import DBUsers
from db.exceptions.user_exception import DBUserNotFoundException, UsernameAlreadyExists
from shemas.update_user import UpdateUser
from shemas.user import User


def create_user(db: Session, user: User) -> int:
    try:
        user_db = DBUsers(username=user.username, password=user.password)
        db.add(user_db)
        db.commit()
        db.refresh(user_db)
        return user_db.id
    except:
        raise UsernameAlreadyExists


def update_username(db: Session, id_: int, update_user: UpdateUser) -> int:
    user = db.query(DBUsers).filter(DBUsers.id == id_).first()
    if user is None:
        raise DBUserNotFoundException()
    try:
        user.username = update_user.username
        db.commit()
        return user.id
    except:
        raise UsernameAlreadyExists


def get_all_users(db: Session) -> list[Type[DBUsers]]:
    return db.query(DBUsers).all()


def get_user_on_id(db: Session, id_: int) -> DBUsers:
    user = db.query(DBUsers).filter(DBUsers.id == id_).first()
    if user is None:
        raise DBUserNotFoundException()
    return user


def get_user_on_login(db: Session, login: str) -> DBUsers:
    user = db.query(DBUsers).filter(DBUsers.username == login).first()
    if user is None:
        raise DBUserNotFoundException()
    return user


def soft_del_user(db: Session, id_: int) -> int:
    db_user = db.query(DBUsers).filter(DBUsers.id == id_).first()
    if db_user is None:
        raise DBUserNotFoundException()
    db_user.is_delete = True
    db.commit()
    return db_user.id

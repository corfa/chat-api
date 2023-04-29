from sqlalchemy.orm import Session

from db.models import DBUsers
from shemas.users import User


def create_user(db: Session, user: User) -> int:
    user_db = DBUsers(username=user.username, password=user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db.id

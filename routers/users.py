from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import helper
from db.models.user import DBUsers
from db.requests.user_requests import create_user
from db.session_db import SessionLocal
from shemas.users import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/user/", tags=["users"])
async def read_users(user: User, db: Session = Depends(get_db)):
    user.password = helper.hash_password(user.password)
    id_user = create_user(db, user)
    return {"id": id_user}



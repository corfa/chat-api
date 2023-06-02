from types import NoneType

from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import helper
from db.requests.chat_requests import get_all_user_chats, get_all_chats
from db.requests.user_requests import create_user, get_all_users, get_user_on_id, soft_del_user, update_username, \
    get_user_on_login
from helper import read_token, verify_password
from routers.depends import get_db, verification
from shemas.update_user import UpdateUser
from shemas.user import User

router = APIRouter()


@router.post("/user/", tags=["users"])
async def create_user_endpoint(user: User, db: Session = Depends(get_db)):
    user.password = helper.hash_password(user.password)
    id_user = create_user(db, user)
    return {"id": id_user}


#
@router.post("/user/auth", tags=["users"])
async def auth_user_endpoint(user: User, db: Session = Depends(get_db)):
    try:
        user_db = get_user_on_login(db, user.username)
        if not verify_password(user.password, user_db.password):
            raise Exception
        token = helper.create_token({"id": user_db.id})
        return {"X-token": token}


    except:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials"
        )


@router.get("/user/", tags=["users"])
async def get_users_endpoint(db: Session = Depends(get_db)):
    all_users = get_all_users(db)
    return {"users": all_users}


@router.get("/user/{id}", tags=["users"])
async def get_user_endpoint(id: int, db: Session = Depends(get_db)):
    user = get_user_on_id(db, id)
    return {"user": user}


@router.put("/user/{id}", tags=["users"])
async def update_user_endpoint(id: int, update_user: UpdateUser, db: Session = Depends(get_db)):
    id_user = update_username(db, id, update_user)
    return {"user_id": id_user}


@router.delete("/user/{id}", tags=["users"])
async def del_user_endpoint(id: int, db: Session = Depends(get_db)):
    id_user = soft_del_user(db, id)
    return {"id": id_user}


@router.get("/user/chat-list/", tags=["users"])
async def get_all_user_chat_endpoint(token: dict = Depends(verification), db: Session = Depends(get_db)):
    user_id = token["id"]
    #chats = get_all_user_chats(db, user_id)
    chats=get_all_chats(db)
    return {"chats": chats}

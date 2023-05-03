from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
import helper
from db.requests.user_requests import create_user, get_all_users, get_user, soft_del_user, update_username
from routers.depends import get_db
from shemas.update_user import UpdateUser
from shemas.user import User

router = APIRouter()


@router.post("/user/", tags=["users"])
async def create_user_endpoint(user: User, db: Session = Depends(get_db)):
    user.password = helper.hash_password(user.password)
    id_user = create_user(db, user)
    return {"id": id_user}


@router.get("/user/", tags=["users"])
async def get_users_endpoint(db: Session = Depends(get_db)):
    all_users = get_all_users(db)
    return {"users": all_users}


@router.get("/user/{id}", tags=["users"])
async def get_user_endpoint(id: int, db: Session = Depends(get_db)):
    user = get_user(db, id)
    return {"user": user}


@router.put("/user/{id}", tags=["users"])
async def update_user_endpoint(id: int, update_user: UpdateUser, db: Session = Depends(get_db)):
    id_user = update_username(db, id, update_user)
    return {"user_id": id_user}


@router.delete("/user/{id}", tags=["users"])
async def del_user_endpoint(id: int, db: Session = Depends(get_db)):
    id_user = soft_del_user(db, id)
    return {"id": id_user}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.requests.chat_requests import create_chat, soft_del_chat, get_all_chats, get_chat_messages
from routers.depends import get_db
from shemas.chat import Chat

router = APIRouter()


@router.post("/chat/", tags=["chat"])
async def create_chat_endpoint(chat: Chat, db: Session = Depends(get_db)):
    id_chat = create_chat(db, chat)
    return {"id": id_chat}


@router.delete("/chat/{id}", tags=["chat"])
async def del_chat_endpoint(id: int, db: Session = Depends(get_db)):
    id_chat = soft_del_chat(db, id)
    return {"id": id_chat}


@router.get("/chat/", tags=["chat"])
async def get_all_chats_endpoint(db: Session = Depends(get_db)):
    all_chat = get_all_chats(db)
    return {"chats": all_chat}


@router.get("/chat/{id}", tags=["chat"])
async def get_chat_messages_endpoint(id: int, db: Session = Depends(get_db)):
    chat_data = get_chat_messages(db, id)
    return chat_data

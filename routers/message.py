from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers.depends import get_db, verification
from routers.socket.active_connections import active_connections, send_message_to_chat
from shemas.message import Message
from db.requests.message_requests import create_message

router = APIRouter()


@router.post("/message", tags=["message"])
async def create_message_endpoint(message: Message, db: Session = Depends(get_db),token: dict = Depends(verification)):
    user_id = token["id"]
    message = create_message(db, message)
    chat_id = message.chat_id
    await send_message_to_chat(chat_id, message.text)

    return {"message": "Message created successfully"}




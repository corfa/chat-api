from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers.depends import get_db, verification
from shemas.reqmessage import ReqMessage, SaveMessage
from db.requests.message_requests import create_message

router = APIRouter()


@router.post("/message", tags=["message"])
async def create_message_endpoint(message: ReqMessage, db: Session = Depends(get_db), token: dict = Depends(verification)):
    user_id = token["id"]
    db_save_message = SaveMessage(text=message.text,chat_id=message.chat_id,user_id=user_id)
    message = create_message(db, db_save_message)
    chat_id = message.chat_id
    return {"message": "ReqMessage created successfully"}

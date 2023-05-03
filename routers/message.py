from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers.depends import get_db
from shemas.message import Message
from db.requests.message_requests import create_message

router = APIRouter()


@router.post("/message", tags=["message"])
async def create_message_endpoint(message: Message, db: Session = Depends(get_db)):
    id_message = create_message(db, message)
    return {"id": id_message}

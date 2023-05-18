from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.websockets import WebSocket

from db.requests.chat_requests import get_all_user_chats, get_chat_ids_for_user
from routers.depends import verification, get_db
from routers.socket.active_connections import active_connections

router = APIRouter()


async def websocket_handler(websocket: WebSocket, db: Session, token: dict, active_connections: dict):
    user_id = token["id"]
    await websocket.accept()
    chat_ids = get_chat_ids_for_user(db=db, user_id=user_id)
    for chat_id in chat_ids:
        if chat_id not in active_connections:
            active_connections[chat_id] = []
        active_connections[chat_id].append(websocket)
    try:
        while True:
            message = await websocket.receive_text()

    finally:
        del active_connections[user_id]


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db), token: dict = Depends(verification)):
    await websocket_handler(websocket, db, token, active_connections)

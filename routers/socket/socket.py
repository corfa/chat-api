from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.websockets import WebSocketDisconnect

from fastapi import WebSocket
from db.requests.message_requests import create_message, get_all_messages_for_chat
from db.requests.user_requests import get_user_on_id
from routers.socket.connect_manager import ConnectManager
from routers.depends import get_db, verification
from shemas.reqmessage import SaveMessage

router = APIRouter()

manager = ConnectManager()


@router.websocket("/chat/{chat_id}")
async def chat_endpoint(websocket: WebSocket, chat_id: int, db: Session = Depends(get_db),
                        token: dict = Depends(verification)):
    user_id = token["id"]
    user = get_user_on_id(db, user_id)
    user_name = user.username

    await websocket.accept()

    await manager.add_connection(websocket, chat_id)

    messages_in_chat = get_all_messages_for_chat(db, chat_id)

    for message in messages_in_chat:
        db_user = get_user_on_id(db, message.user_id)
        data = f"сообщение от пользоватля {db_user.username} : {message.text}"
        await websocket.send_text(data)

    try:
        while True:
            data = await websocket.receive_text()
            message = SaveMessage(user_id=user_id, chat_id=chat_id, text=data)
            create_message(db, message)
            await manager.send_message_in_chat(chat_id, message.text, user_name)
    except WebSocketDisconnect:
        await manager.remove_connection(websocket, chat_id)

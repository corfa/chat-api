import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.websockets import WebSocketDisconnect

from fastapi import WebSocket
from db.requests.message_requests import create_message, get_all_messages_for_chat
from db.requests.user_requests import get_user_on_id
from helper import read_token
from routers.socket.connect_manager import ConnectManager
from routers.depends import get_db
from shemas.reqmessage import SaveMessage

router = APIRouter()

manager = ConnectManager()


@router.websocket("/chat/{chat_id}")
async def chat_endpoint(websocket: WebSocket, chat_id: int, db: Session = Depends(get_db)):
    try:

        headers = websocket.headers
        token = headers.get("sec-websocket-protocol")
        user = read_token(token)
        user_id = user["id"]
        await websocket.accept()
        user = get_user_on_id(db, user_id)
        user_name = user.username

        await manager.add_connection(websocket, chat_id)
        messages_in_chat = get_all_messages_for_chat(db, chat_id)

        for message in messages_in_chat:
            db_user = get_user_on_id(db, message.user_id)
            data = {"id": message.id, "user": db_user.username, "text": message.text}
            json_data = json.dumps(data)
            await websocket.send_text(json_data)

        while True:
            data = await websocket.receive_text()
            message = SaveMessage(user_id=user_id, chat_id=chat_id, text=data)
            id = create_message(db, message)
            data = {"id": id, "user": user_name, "text": message.text}
            await manager.send_message_in_chat(chat_id, data)

    except WebSocketDisconnect:
        await manager.remove_connection(websocket, chat_id)
    except:
        await websocket.close()

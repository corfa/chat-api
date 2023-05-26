from websocket import WebSocket


class ConnectManager:
    def __init__(self):
        self.active_connections_chats = {}

    async def add_connection(self, websocket: WebSocket, chat_id: int):
        if chat_id not in self.active_connections_chats:
            self.active_connections_chats[chat_id] = []
        self.active_connections_chats[chat_id].append(websocket)

    async def remove_connection(self, websocket: WebSocket, chat_id: int):
        self.active_connections_chats[chat_id].remove(websocket)

        if len(self.active_connections_chats[chat_id]) == 0:
            self.active_connections_chats.pop(chat_id)

    async def send_message_in_chat(self, chat_id, data, sendler):
        for connection in self.active_connections_chats[chat_id]:
            message = f"сообщение от пользоватля {sendler} : {data}"
            await connection.send_text(message)

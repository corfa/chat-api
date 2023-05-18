active_connections = {}


async def send_message_to_chat(chat_id: int, message_text: str) -> int:
    chat_connections = active_connections.get(chat_id, [])
    for connection in chat_connections:
        try:
            await connection.send(message_text)
        except Exception:
            pass
    return chat_id

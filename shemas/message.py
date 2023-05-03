from pydantic import BaseModel


class Message(BaseModel):
    text: str
    user_id: int
    chat_id: int


from pydantic import BaseModel


class ReqMessage(BaseModel):
    text: str
    chat_id: int


class SaveMessage(BaseModel):
    text: str
    chat_id: int
    user_id: int

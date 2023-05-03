from pydantic import BaseModel


class Chat(BaseModel):
    name: str

from fastapi import FastAPI

from routers import user, chat, message

app = FastAPI()

app.include_router(user.router)
app.include_router(chat.router)
app.include_router(message.router)

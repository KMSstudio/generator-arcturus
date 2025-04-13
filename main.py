from fastapi import FastAPI
from router import chat, version

app = FastAPI()
app.include_router(chat.router)
app.include_router(version.router)
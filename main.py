from fastapi import FastAPI
from router import chat, version
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(chat.router)
app.include_router(version.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (개발용)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
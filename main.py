from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import settings
from routers import (
    auth_router,
    question_router,
    answer_router,
)

app = FastAPI(title="Pybo API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://localhost",
        "http://localhost:80",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router 등록
app.include_router(auth_router.router)
app.include_router(question_router.router)
app.include_router(answer_router.router)
from fastapi import FastAPI

from routers import (
    auth_router,
    question_router,
    answer_router,
)

app = FastAPI(title="Pybo API")

app.include_router(auth_router.router)
app.include_router(question_router.router)
app.include_router(answer_router.router)
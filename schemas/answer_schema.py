from datetime import datetime

from pydantic import BaseModel, ConfigDict


# 답변 등록
class AnswerCreate(BaseModel):
    content: str


# 답변 수정
class AnswerUpdate(BaseModel):
    content: str

# 답변 조회
class AnswerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    create_date: datetime
    question_id: int
    user_id: int
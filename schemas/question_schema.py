from datetime import datetime

from pydantic import BaseModel, ConfigDict

from schemas.answer_schema import AnswerResponse
from schemas.auth_schema import UserResponse

# 질문 등록
class QuestionCreate(BaseModel):
    subject: str
    content: str


# 질문 수정
class QuestionUpdate(BaseModel):
    subject: str
    content: str


# 질문 목록 조회
class QuestionListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject: str
    create_date: datetime

    user: UserResponse

# 질문 상세 조회
class QuestionDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject: str
    content: str
    create_date: datetime

    user: UserResponse
    answers: list[AnswerResponse]
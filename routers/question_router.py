from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import (
    get_db,
    get_current_user
)

from models import User

from services.question_service import QuestionService
from schemas.question_schema import (
    QuestionCreate,
    QuestionUpdate,
    QuestionListResponse,
    QuestionDetailResponse,
)

router = APIRouter(
    prefix="/questions",
    tags=["Question"]
)


@router.get("", response_model=list[QuestionListResponse])
def get_questions(
    db: Session = Depends(get_db)
):
    service = QuestionService(db)
    return service.get_all()


@router.get("/{question_id}", response_model=QuestionDetailResponse)
def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    service = QuestionService(db)
    return service.get(question_id)


@router.post("", response_model=QuestionDetailResponse, status_code=201)
def create_question(
    request: QuestionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = QuestionService(db)
    return service.create(request, current_user.id)


@router.put("/{question_id}", response_model=QuestionDetailResponse)
def update_question(
    question_id: int,
    request: QuestionUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = QuestionService(db)
    return service.update(question_id, request, current_user.id)


@router.delete("/{question_id}", status_code=204)
def delete_question(
    question_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = QuestionService(db)
    service.delete(question_id, current_user.id)
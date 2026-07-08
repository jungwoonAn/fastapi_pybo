from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import (
    get_db,
    get_current_user
)

from models import User

from services.answer_service import AnswerService

from schemas.answer_schema import (
    AnswerCreate,
    AnswerUpdate,
    AnswerResponse,
)

router = APIRouter(
    prefix="/answers",
    tags=["Answer"]
)


@router.post("/{question_id}", response_model=AnswerResponse, status_code=201)
def create_answer(
    question_id: int,
    request: AnswerCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    service = AnswerService(db)
    return service.create(
        question_id,
        request,
        current_user.id
    )


@router.put("/{answer_id}", response_model=AnswerResponse)
def update_answer(
    answer_id: int,
    request: AnswerUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    service = AnswerService(db)
    return service.update(answer_id, request, current_user.id)


@router.delete("/{answer_id}", status_code=204)
def delete_answer(
    answer_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    service = AnswerService(db)
    service.delete(answer_id, current_user.id)
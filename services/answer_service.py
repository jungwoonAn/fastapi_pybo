from fastapi import HTTPException, status

from models import Answer

from repositories.answer_repository import AnswerRepository
from repositories.question_repository import QuestionRepository

from schemas.answer_schema import (
    AnswerCreate,
    AnswerUpdate,
)

from services.base_service import BaseService


class AnswerService(BaseService):

    def __init__(self, db):
        super().__init__(db)

        self.answer_repository = AnswerRepository(db)
        self.question_repository = QuestionRepository(db)

    def create(
        self,
        question_id: int,
        request: AnswerCreate,
        user_id: int
    ):

        question = self.question_repository.get(question_id)

        if question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="질문이 존재하지 않습니다."
            )

        answer = Answer(
            content=request.content,
            question_id=question_id,
            user_id=user_id
        )

        self.answer_repository.create(answer)
        self.commit_and_refresh(answer)

        return answer

    def update(
        self,
        answer_id: int,
        request: AnswerUpdate,
        user_id: int
    ):

        answer = self.answer_repository.get(answer_id)

        if answer.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="수정 권한이 없습니다."
            )

        answer.content = request.content

        self.commit_and_refresh(answer)

        return answer

    def delete(self, answer_id: int, user_id: int):

        answer = self.answer_repository.get(answer_id)

        if answer.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="삭제 권한이 없습니다."
            )

        self.answer_repository.delete(answer)
        self.commit()

        return {
            "message": "삭제 완료"
        }
from fastapi import HTTPException, status

from models import Question

from repositories.question_repository import QuestionRepository

from schemas.question_schema import (
    QuestionCreate,
    QuestionUpdate,
)

from services.base_service import BaseService


class QuestionService(BaseService):

    def __init__(self, db):
        super().__init__(db)
        self.repository = QuestionRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get(self, question_id: int):

        question = self.repository.get(question_id)

        if question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="질문이 존재하지 않습니다."
            )

        return question

    def create(
        self,
        request: QuestionCreate,
        user_id: int
    ):

        question = Question(
            subject=request.subject,
            content=request.content,
            user_id=user_id
        )

        self.repository.create(question)
        self.commit_and_refresh(question)

        return question

    def update(
        self,
        question_id: int,
        request: QuestionUpdate,
        user_id: int
    ):

        question = self.get(question_id)

        if question.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="수정 권한이 없습니다."
            )

        question.subject = request.subject
        question.content = request.content

        self.commit_and_refresh(question)

        return question

    def delete(self, question_id: int, user_id: int):

        question = self.get(question_id)

        if question.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="삭제 권한이 없습니다."
            )

        self.repository.delete(question)
        self.commit()
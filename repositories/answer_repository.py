from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Answer


class AnswerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, answer: Answer) -> None:
        self.db.add(answer)

    def get(self, answer_id: int) -> Answer | None:
        return self.db.get(Answer, answer_id)

    def get_by_question(self, question_id: int) -> list[Answer]:

        stmt = (
            select(Answer)
            .where(Answer.question_id == question_id)
            .order_by(Answer.create_date)
        )

        return list(self.db.scalars(stmt).all())

    def delete(self, answer: Answer) -> None:
        self.db.delete(answer)
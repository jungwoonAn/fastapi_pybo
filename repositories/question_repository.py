from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Question


class QuestionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, question: Question) -> None:
        self.db.add(question)

    def get(self, question_id: int) -> Question | None:
        return self.db.get(Question, question_id)

    def get_all(self) -> list[Question]:
        stmt = (
            select(Question)
            .order_by(Question.create_date.desc())
        )
        return list(self.db.scalars(stmt).all())

    def delete(self, question: Question) -> None:
        self.db.delete(question)
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User


class AuthRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User) -> None:
        self.db.add(user)

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)

    def get_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        return self.db.scalar(stmt)

    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.db.scalar(stmt)
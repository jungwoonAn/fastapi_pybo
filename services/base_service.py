from sqlalchemy.orm import Session


class BaseService:

    def __init__(self, db: Session):
        self.db = db

    def commit(self):
        """
        트랜잭션 커밋
        """

        try:
            self.db.commit()

        except Exception:
            self.db.rollback()
            raise

    def refresh(self, entity):
        """
        엔티티 새로고침
        """

        self.db.refresh(entity)

    def commit_and_refresh(self, entity):
        """
        Commit 후 Refresh
        """

        self.commit()
        self.refresh(entity)
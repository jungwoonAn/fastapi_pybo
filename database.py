from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from sqlalchemy.orm import declarative_base

from config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 모든 ORM 모델의 부모 클래스(Base Class)를 만드는 코드
# Base=declarative_base()  # SQLAlchemy 1.0

# SQLAlchemy 2.0에서는 declarative_base() 대신 DeclarativeBase 클래스를 상속하는 방식을 권장
class Base(DeclarativeBase):
    pass
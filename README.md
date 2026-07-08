# Pybo FastAPI REST API

## 프로젝트 소개

**Pybo**는 『Do it! 점프 투 플라스크』의 게시판 예제를 기반으로 **Flask
프로젝트를 FastAPI + REST API 구조로 리팩토링**한 프로젝트입니다.

기존 Flask의 Template 기반 구조를 다음과 같은 현대적인 백엔드 아키텍처로
변경하였습니다.

-   FastAPI
-   SQLAlchemy 2.0 ORM
-   Alembic Migration
-   JWT Authentication
-   Repository Pattern
-   Service Layer
-   Dependency Injection
-   Pydantic Schema

------------------------------------------------------------------------

# 기술 스택

  구분             기술
  ---------------- -------------------
  Language         Python 3.13
  Framework        FastAPI
  ORM              SQLAlchemy 2.0
  Migration        Alembic
  Validation       Pydantic v2
  Authentication   JWT (python-jose)
  Password Hash    Passlib + bcrypt
  ASGI Server      Uvicorn
  Database         SQLite

------------------------------------------------------------------------

# 프로젝트 구조

``` text
pybo/
├── main.py
├── config.py
├── database.py
├── dependencies.py
├── models.py
├── routers/
├── services/
├── repositories/
├── schemas/
├── utils/
├── migrations/
├── .env
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# 아키텍처

``` text
React
  │
  ▼
FastAPI Router
  │
  ▼
Service
  │
  ▼
Repository
  │
  ▼
SQLAlchemy ORM
  │
  ▼
Database
```

## 실행

``` bash
git clone <repository-url>
cd pybo

python -m venv .venv
pip install -r requirements.txt

alembic init migrations
alembic revision --autogenerate
alembic upgrade head

uvicorn main:app --reload
```

Swagger: http://localhost:8000/docs
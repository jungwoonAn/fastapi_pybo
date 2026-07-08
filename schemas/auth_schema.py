from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


# 회원가입
class SignupRequest(BaseModel):
    username: str
    password: str
    email: EmailStr


# 로그인
class LoginRequest(BaseModel):
    username: str
    password: str


# 회원 조회
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Pydantic v2

    id: int
    username: str
    email: EmailStr
    create_date: datetime


# 로그인 응답
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


# Refresh Token 요청
class RefreshTokenRequest(BaseModel):
    refresh_token: str
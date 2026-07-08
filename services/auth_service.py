from fastapi import HTTPException, status

from models import User
from repositories.auth_repository import AuthRepository

from utils.jwt import decode_token
from utils.jwt_blacklist import jwt_blacklist

from schemas.auth_schema import (
    SignupRequest,
    LoginRequest,
)

from utils.security import (
    hash_password,
    verify_password,
)

from utils.jwt import (
    create_access_token,
    create_refresh_token,
)

from services.base_service import BaseService


class AuthService(BaseService):

    def __init__(self, db):
        super().__init__(db)
        self.repository = AuthRepository(db)

    def signup(self, request: SignupRequest):

        if self.repository.get_by_username(request.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="이미 존재하는 사용자입니다."
            )

        if self.repository.get_by_email(request.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="이미 사용중인 이메일입니다."
            )

        user = User(
            username=request.username,
            password=hash_password(request.password),
            email=request.email
        )

        self.repository.create_user(user)
        self.commit_and_refresh(user)

        return {
            "message": "회원가입 완료"
        }

    def login(self, request: LoginRequest):

        user = self.repository.get_by_username(request.username)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="아이디 또는 비밀번호가 올바르지 않습니다."
            )

        if not verify_password(
            request.password,
            user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="아이디 또는 비밀번호가 올바르지 않습니다."
            )

        return {
            "access_token": create_access_token(user.id),
            "refresh_token": create_refresh_token(user.id),
            "token_type": "bearer"
        }

    def logout(self, token: str):

        payload = decode_token(token)
        jti = payload["jti"]
        jwt_blacklist.add(jti)

        return {
            "message": "로그아웃 되었습니다."
        }
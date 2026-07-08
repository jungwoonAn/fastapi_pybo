from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from dependencies import get_db
from schemas.common_schema import MessageResponse
from schemas.auth_schema import (
    SignupRequest,
    LoginRequest,
    TokenResponse,
)

from services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

@router.post("/signup", response_model=MessageResponse, status_code=201)
def signup(
    request: SignupRequest,
    db: Session = Depends(get_db)
):
    service = AuthService(db)
    return service.signup(request)


@router.post("/login", response_model=TokenResponse)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    service = AuthService(db)
    return service.login(request)

@router.post("/logout", response_model=MessageResponse)
def logout(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    service = AuthService(db)
    return service.logout(token)
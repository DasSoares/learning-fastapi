from typing import Annotated
from datetime import timedelta

from fastapi import status
from fastapi import Depends
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.forms.auth_jwt import User, Token
from app.auth.jwt import fake_users_db
from app.auth.jwt import ACCESS_TOKEN_EXPIRE_MINUTES
from app.auth.jwt import authenticate_user, create_access_token, get_current_user


router = APIRouter(
    prefix="/jwt",
    tags=["jwt"]
)

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/hello")
async def hello(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return "Hello, Auth Jwt"

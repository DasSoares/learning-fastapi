from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


# your code here
users = {
    "admin": "secret"
}


security = HTTPBasic()
router = APIRouter(
    prefix="/basic",
    tags=["basic"]
)

# Checa se o usuário 
def check_user(credentials: HTTPBasicCredentials = Depends(security)):
    for user, password in users.items():
        if credentials.username != user or credentials.password != password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    return credentials.username


# autenticação basica
@router.get("/")
async def hello(username: str = Depends(check_user)):
    return "Hello, Basic Authentication!"

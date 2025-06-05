
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic

from app.auth.basic import check_user


# your code here
security = HTTPBasic()
router = APIRouter(
    prefix="/basic",
    tags=["basic"]
)

# autenticação basica
@router.get("/")
async def hello(username: str = Depends(check_user)):
    return "Hello, Basic Authentication!"
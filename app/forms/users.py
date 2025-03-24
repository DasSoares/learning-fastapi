from . import BaseModel, Field
from typing import Optional

# your code here
# os forms são como os objetos
# utilizados como modelo de envio e propriedades que devem ser enviados
class Message(BaseModel):
    message: str


class User(BaseModel):
    id: Optional[int] = Field(...)
    name: str = Field(...)
    email: str = Field(...)


class CreateUser(User):
    id: int = Field(None, exclude=True)


class UpdateUser(BaseModel):
    name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)

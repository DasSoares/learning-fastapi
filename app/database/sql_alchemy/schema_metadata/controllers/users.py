from sqlalchemy import select, create_engine
from app.database.sql_alchemy.schema_metadata.models import t_user
from app.database.connection import engine, create_engine
from app.database.sql_alchemy.schema_metadata.controllers.crud_model import CrudModel

# your code here
class UserController(CrudModel):
    
    def __init__(self, session=None):
        super().__init__(session, t_user)
    
    def create(self, name: str, email: str):
        return self.__insert__(
            name=name,
            email=email
        )
    
    def update(self, id: int, name: str, email: str):
        return self.__edit__(
            id=id,
            name=name,
            email=email
        )

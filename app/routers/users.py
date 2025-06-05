from typing import Union

from fastapi import APIRouter, Path
from app.forms.users import User, CreateUser, UpdateUser
from app.forms import NotFoundMessage, BadRequestMessage, InternalServerErrorMessage
from faker import Faker
from app.exceptions import NotFoundException, BadRequestException, InternalServerErrorException
# from validate_docbr import CPF

from app.database.sql_alchemy.schema_metadata.controllers.users import UserController

# your code here
# Utilizada para agrupar e separar rotas
router = APIRouter(
    prefix="/users",  # Barramento do endpoint que será chamada
    tags=["users"],   # as tags são como grupos, utilizadas para separar uma das outras
)

# Modelo de respostas, adicione os retornos para cada tipo de status: 200, 300, 400, 500 e etc
responses_errors = {
    400: {
        "model": BadRequestMessage
    },
    404: {
        "model": NotFoundMessage
    },
    500: {
        "model": InternalServerErrorMessage
    },
}


@router.get(
    "/",
    response_model=Union[list[User], list],  # Lista ou array de usuário ou, dicionário. Mas sempre coloque o modelo de retorno para deixar o código mais conciso
    description="Retorna a lista de usuários",
)
async def user_list():
    uc = UserController()
    return uc.all()


@router.get(
    "/{id}",
    response_model=User,
    description="Busca o usuário na lista e retorna caso exista",
    responses=responses_errors,
)
async def get_user(
    id: int,
    # user_id: int = Query(None, description="Id do usuário em Query parameters") # exemplo de query parameters
):
    uc = UserController()
    user = uc.get(id)
    if not user:
        raise NotFoundException(detail="Usuário não encontrado")
    return user


@router.post(
    "/",
    description="Cria usuário",
    # response_model=User,
    status_code=201,
    responses=responses_errors,
)
async def create_user(user: CreateUser):
    try:
        uc = UserController()
        uc.create(user.name.title(), user.email)
        uc.session.commit()
    except Exception as e:
        return BadRequestException(f"Erro ao inserir registro no banco. erro: {e.args}")
    return


@router.put(
    "/{id}",
    description="Altera os dados do registro do usuário",
    status_code=204,
)
async def update_user(id: int, user: UpdateUser):
    uc = UserController()
    usr = uc.get(id)
    dic = dict(name="", email="")
    if usr:
        message = "Usuário alterado com sucesso"
        isUpdated = False

        for key, value in user.model_dump().items():
            if value and value != usr.get(key):
                dic[key] = value
                isUpdated = True
            else:
                dic[key] = usr.get(key)

        if not isUpdated:
            return BadRequestException(detail="Não foi possível alterar os dados do usuário")
        
        uc.update(id, dic.get("name"), dic.get("email"))
        uc.session.commit()
        return
    return NotFoundException(detail="Usuário não encontrado")


@router.delete(
    "/{id}",
    description="Exclui usuário",
    status_code=204,
    responses=responses_errors,
)
async def delete_user(
    id: int = Path(..., description="ID do usuário")
):
    # operador walrus ':=' (ou operador de atribuição em expressão).
    # foi adicionado na versão 3.8, é permitido utilizar apenas em condições
    # a utilização dele é tornar o código mais conciso
    # Utilize com moderação! Aqui é apenas um exemplo
    uc = UserController()
    if (is_removed := uc.delete(id)):
        uc.session.commit()
        return
    return NotFoundException(detail="Usuário não encontrado")


@router.post(
    "/generates_user",
    description="Cria usuário",
    status_code=201,
)
async def generates_user():
    fk = Faker()
    # doc = CPF()
    uc = UserController()
    
    name = fk.name()
    email = name.lower().replace(" ", "") + "@" + fk.email().split('@')[1]
    try:
        uc.create(
            name=name,
            email=email
        )
        uc.session.commit()
    except Exception as e:
        return BadRequestException(detail=f"Erro ao inserir registro no banco. erro: {e.args}")
    return


# def find_user_or_none(id: int) -> dict | None:
#     """ Busca o usuário ou nulo """
#     return next(filter(lambda usr: usr.get("id") == id, users), None)

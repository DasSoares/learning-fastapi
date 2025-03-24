from fastapi import APIRouter, Query, Path
from fastapi.responses import JSONResponse
from app.forms.users import User, CreateUser, UpdateUser, Message
from faker import Faker
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
    404: {
        "model": Message
    }
}


@router.get(
    "/",
    response_model=list[
        User
    ] | list,  # Lista ou array de usuário ou, dicionário. Mas sempre coloque o modelo de retorno para deixar o código mais conciso
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
        message_error = Message(message="Usuário não encontrado")
        return JSONResponse(content=message_error.model_dump(), status_code=404)
    return user


@router.post(
    "/",
    description="Cria usuário",
    # response_model=User,
    status_code=204,
    responses=responses_errors,
)
async def create_user(user: CreateUser):
    try:
        uc = UserController()
        uc.create(user.name.title(), user.email)
        uc.session.commit()
    except Exception as e:
        return JSONResponse(Message(message=f"Erro ao inserir registro no banco. erro: {e.args}").model_dump(), 400)
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
            message = "Não foi possível alterar os dados do usuário"
            return JSONResponse(Message(message=message).model_dump(), status_code=400)
        uc.update(id, dic.get("name"), dic.get("email"))
        uc.session.commit()
        return
    return JSONResponse(
        Message(message="Usuário não encontrado").model_dump(), status_code=404
    )


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
    return JSONResponse(
        Message(message="Usuário não encontrado").model_dump(), status_code=404
    )


@router.post(
    "/generates_user",
    description="Cria usuário",
    status_code=204,
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
        return JSONResponse(Message(message=f"Erro ao inserir registro no banco. erro: {e.args}").model_dump(), 400)
    return


# def find_user_or_none(id: int) -> dict | None:
#     """ Busca o usuário ou nulo """
#     return next(filter(lambda usr: usr.get("id") == id, users), None)

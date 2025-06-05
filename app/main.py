import time
import asyncio
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# metodos
from app.routers.auth_basic import router as router_basic_exemple
from app.routers.auth_jwt import router as router_jwt_exemple
from app.routers.users import router as users_router

# Variaveis
from app.properties import URL, PORT, APP_ENV
from app.middleware.exception_handlers import setup_exception_handler


# your code here
doc_config = {}
if APP_ENV not in ("dev", "local"):
    doc_config = {
        "docs_url": None,
        "redoc_url": None,
        "openapi_url": None,
    }

# inicializa a Aplicação, Running
app = FastAPI(
    title="FastAPI",
    description="Teste FastAPI",
    servers=[
        { "url": f"{URL}:{PORT}", "description": "API Local" },
    ],
    **doc_config,
)
setup_exception_handler(app)

# Hosts permitidos acesso à API
origins = [
    "*",
    f"{URL}:{PORT}",
]

# é um componente ou função intermediária que intercepta e processa requisições ou respostas em um fluxo de execução.
# Ele funciona como uma camada entre o cliente (por exemplo, navegador) e a aplicação principal,
# permitindo realizar tarefas adicionais antes ou depois que a lógica principal seja executada.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adiciona rotas na API para serem encontradas, necessário para cada rota criada
app.include_router(users_router)
app.include_router(router_basic_exemple) # basic authentication
app.include_router(router_jwt_exemple)   # jwt authentication
                                         # quais outros tipos de autenticação existem?


# Configura o logging básico
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log"),
    ],
)

logger = logging.getLogger(__name__)

# endpoint padrão
# > http://127.0.0.1:8000/
@app.get("/")
async def hello():
# def hello():
    # await asyncio.sleep(10)
    # time.sleep(10)
    return "Hello, world!"


if __name__ == "__main__":
    # main, inicia o servidor a partir deste arquivo,
    # aqui você pode implementar o arquivo .env e informar IP, Porta e etc da variavel de ambiente
    uvicorn.run(
        app=app,
        host=URL,
        port=PORT,
    )

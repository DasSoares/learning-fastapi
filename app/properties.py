import os
from dotenv import load_dotenv


if not load_dotenv("app/.env"):
    raise Exception("Não foi possível encontrar as variaveis de ambiente!")


APP_ENV = os.getenv("APP_ENV")
URL = os.getenv("URL")
PORT = os.getenv("PORT")

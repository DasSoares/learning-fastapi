import os
from dotenv import load_dotenv


if not load_dotenv("app/.env"):
    raise Exception("Não foi possível encontrar as variaveis de ambiente!")

URL = os.getenv("URL")
PORT = os.getenv("PORT")

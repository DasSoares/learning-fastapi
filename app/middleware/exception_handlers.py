import logging
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from app.exceptions import NotFoundException, BadRequestException, UnauthorizedException, HTTPException


# Exceções personalizadas para tratamento de erros
# Essas exceções herdam de HTTPException e podem ser usadas para retornar respostas específicas
# com códigos de status HTTP apropriados e mensagens de erro personalizadas.
def setup_exception_handler(app: FastAPI):
    """ Configura o tratamento de exceções para a aplicação """
    
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        """ Tratamento de exceções HTTP """
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": str(exc.detail)},
        )
    
    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(request: Request, exc: Exception):
        """ Tratamento de exceções para recurso não encontrado """
        logging.error(f"{exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": str(exc.detail)},
        )
    
    @app.exception_handler(BadRequestException)
    async def bad_request_exception_handler(request: Request, exc: Exception):
        """ Tratamento de exceções para requisição inválida """
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": str(exc.detail)},
        )
    
    @app.exception_handler(UnauthorizedException)
    async def unauthorized_exception_handler(request: Request, exc: Exception):
        """ Tratamento de exceções para não autorizado """
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": str(exc.detail)},
        )

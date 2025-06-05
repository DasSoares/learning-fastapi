from pydantic import BaseModel, Field

class BadRequestMessage(BaseModel):
    detail: str

class NotFoundMessage(BaseModel):
    detail: str

class UnauthorizedMessage(BaseModel):
    detail: str
    
class ForbiddenMessage(BaseModel):
    detail: str

class InternalServerErrorMessage(BaseModel):
    detail: str

class MethodNotAllowedMessage(BaseModel):
    detail: str

class UnprocessableEntityMessage(BaseModel):
    detail: str
    
class ConflictMessage(BaseModel):
    detail: str

class TooManyRequestsMessage(BaseModel):
    detail: str

class ServiceUnavailableMessage(BaseModel):
    detail: str

class GatewayTimeoutMessage(BaseModel):
    detail: str

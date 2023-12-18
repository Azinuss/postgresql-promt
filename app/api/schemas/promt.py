# Все возможные ответы и запросы API
from pydantic import BaseModel


class PromtCreateRequestSchema(BaseModel):
    name: str
    description: str
    promt:str
    creator:str 

class PromtCreateResponseSchema(BaseModel):
    id:int
    name:str
    description:str
    promt:str
    creator:str 
    create_time:str
    update_time:str


class PromtDeleteRequestSchema(BaseModel):
    name: str

class PromtDeleteResponseSchema(BaseModel):
    ...

class PromtReadRequestSchema(BaseModel):
    ...

class PromtReadResponseSchema(BaseModel):
    ...

class PromtUpdateRequestSchema(BaseModel): # надо передать старое название и новые данные
    old_name:str
    name:str
    description:str
    promt:str
    creator:str 

class PromtUpdateResponseSchema(BaseModel):
    id:int
    name:str
    description:str
    promt:str
    creator:str 
    create_time:str
    update_time:str

class PromtGetByIdRequestSchema(BaseModel):
    id:int

class PromtGetByIdResponseSchema(BaseModel):
    id:int
    name:str
    description:str
    promt:str
    creator:str 
    create_time:str
    update_time:str

# class PromtSchema(BaseModel):
#     id:int
#     name:str
#     description:str
#     promt:str
#     creator:str 
#     create_time:str
#     update_time:str
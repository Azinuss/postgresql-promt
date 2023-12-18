from pydantic import BaseModel


class Promt(BaseModel):
    id:int
    name:str
    description:str
    promt:str
    creator:str 
    create_time:str
    update_time:str
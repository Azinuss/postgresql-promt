#Хранит информацию о полях в БД
from typing import Optional

from sqlmodel import SQLModel, Field

class PromtModel(SQLModel, table=True):
    
    __tablename__ = "promt"

    id: Optional[int] = Field(
        primary_key=True,
        default=None
    )

    name:str =Field(
        max_length=100,
        unique=True
    )

    description:str =Field(
        max_length=500,
        unique=True  
    )
    promt:str =Field(
        max_length=1000,
        unique=True  
    )
    creator:str =Field(
        max_length=100,
        unique=True   
    )

    create_time:str =Field(
        max_length=100,
        unique=True  
    )

    update_time:str =Field(
        max_length=100,
        unique=True  
    )
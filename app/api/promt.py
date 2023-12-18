from typing import  List, Union

from fastapi import APIRouter, Depends

from domain.promt import Promt
from api.schemas.promt import PromtCreateRequestSchema, PromtCreateResponseSchema
from api.schemas.promt import PromtDeleteRequestSchema, PromtDeleteResponseSchema
from api.schemas.promt import PromtReadRequestSchema, PromtReadResponseSchema
from api.schemas.promt import PromtUpdateRequestSchema, PromtUpdateResponseSchema
from api.schemas.promt import PromtGetByIdRequestSchema, PromtGetByIdResponseSchema 
from core.dependencies.persistance import promt_persistence_dependency

from persistence.common import PromtPersistence

router = APIRouter()

@router.post("/create", summary="Create promt", description="Add new in DB promt for sale",
             response_model=PromtCreateResponseSchema)
async def create_promt(create_request: PromtCreateRequestSchema,
                       promt_persistence: PromtPersistence = Depends(promt_persistence_dependency)) -> PromtCreateRequestSchema:
    promt = promt_persistence.create(name=create_request.name, description=create_request.description,
                                     promt=create_request.promt, creator=create_request.creator)# Решить где определять время создания тут или в части БД
    return PromtCreateResponseSchema(id=promt.id,name=promt.name, description=promt.description,
                                     promt=promt.promt, creator=promt.creator, create_time=promt.create_time, update_time=promt.update_time)


@router.delete("/delete", summary="Delete promt", description="Delete promt from DB",
             response_model=PromtDeleteResponseSchema)
async def delete_promt(delete_request: PromtDeleteRequestSchema,
                       promt_persistence: PromtPersistence = Depends(promt_persistence_dependency)) -> PromtDeleteRequestSchema:
    promt_persistence.delete(name=delete_request.name)
    return PromtDeleteResponseSchema()


@router.get("/list", summary="List of promts", description= "Get list of all promts",
            response_model=List[Promt])
async def list_promt(promt_persistence: PromtPersistence = Depends(promt_persistence_dependency)) -> List[Promt]:
    promts = promt_persistence.list_promt()
    return [Promt(id=promt.id ,name=promt.name, description=promt.description,
                    promt=promt.promt, creator=promt.creator, create_time=promt.create_time, update_time=promt.update_time) for promt in promts]


@router.post("/update",summary="Update promt", description="Update promt in DB", response_model=PromtUpdateResponseSchema)
async def update_promt(update_request:PromtUpdateRequestSchema, 
                       promt_persistence: PromtPersistence = Depends(promt_persistence_dependency)) -> Promt:
    promt = promt_persistence.update(old_name=update_request.old_name, name=update_request.name, 
                                     descrition=update_request.description,promt=update_request.promt,creator=update_request.creator)
    return PromtUpdateResponseSchema(id=promt.id ,name=promt.name, description=promt.description,
                                     promt=promt.promt, creator=promt.creator, create_time=promt.create_time, update_time=promt.update_time)


@router.post("/{promt_id}", summary="Get promt", description="Get promt by id",
            response_model=Union[PromtGetByIdResponseSchema, None])
async def get_promt_by_id(get_by_id_request:PromtGetByIdRequestSchema,
                    promt_persistence: PromtPersistence = Depends(promt_persistence_dependency)) -> Union[PromtGetByIdResponseSchema, None]: #Заменить None на другой ответ?
    promt = promt_persistence.get_promt_by_id(get_by_id_request.id)
    print(promt)
    if promt != None:
        return PromtGetByIdResponseSchema(id=promt.id ,name=promt.name, description=promt.description, promt=promt.promt,
                                          creator=promt.creator, create_time=promt.create_time, update_time=promt.update_time)
    else:
        return None

    
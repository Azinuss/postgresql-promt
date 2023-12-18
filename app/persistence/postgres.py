from datetime import datetime

from typing import List, Union

from sqlmodel import Session, select

from db.models.promt import PromtModel
from domain.promt import Promt
from persistence.common import PromtPersistence


class PostgresPromtPersistence(PromtPersistence):
    def __init__(self,session: Session):
        self.__session = session

    def create(self, name:str, description:str, promt:str, creator:str) -> Promt:
        promt_model = PromtModel(name=name, description=description, promt=promt, creator=creator,
                                create_time=str(datetime.now()), update_time=str(datetime.now()))
        self.__session.add(promt_model)
        self.__session.commit()
        return Promt(id=promt_model.id, name=promt_model.name, description=promt_model.description, promt=promt_model.promt,
                      creator=promt_model.creator, create_time=promt_model.create_time, update_time=promt_model.update_time)
    
    def delete(self, name:str) -> None:
        query = select(PromtModel).where(PromtModel.name == name)
        promt_model = self.__session.exec(query).first()
        self.__session.delete(promt_model)
        self.__session.commit()
        return None

    def update(self, old_name: str, name:str, descrition:str, 
                promt:str, creator:str) -> Promt:
        query = select(PromtModel).where(PromtModel.name == old_name)
        promt_model = self.__session.exec(query).first()
        promt_model.name = name
        promt_model.description = descrition
        promt_model.promt = promt
        promt_model.creator = creator
        promt_model.update_time = str(datetime.now())
        self.__session.add(promt_model)
        self.__session.commit()
        return Promt(id=promt_model.id, name=promt_model.name, description=promt_model.description, promt=promt_model.promt,
                     creator=promt_model.creator, create_time=promt_model.create_time, update_time=promt_model.update_time)


    def get_promt_by_id(self, promt_id:int) -> Union[Promt,None]:
        query = select(PromtModel).where(PromtModel.id == promt_id)
        promt_model = self.__session.exec(query).first()
        if promt_model != None:
            return Promt(id=promt_model.id, name=promt_model.name, description=promt_model.description, promt=promt_model.promt,
                         creator=promt_model.creator, create_time=promt_model.create_time, update_time=promt_model.update_time)
        else:
            return None

    def list_promt(self) -> List[Promt]:
        query = select(PromtModel)
        promt_models = self.__session.exec(query).all() 
        return [Promt(id=promt_model.id, name=promt_model.name, description=promt_model.description, promt=promt_model.promt,
                     creator=promt_model.creator, create_time=promt_model.create_time, update_time=promt_model.update_time) 
                     for promt_model in promt_models]
    
    
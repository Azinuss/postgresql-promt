from abc import ABC, abstractmethod
from typing import List

from domain.promt import Promt




class PromtPersistence(ABC):
    @abstractmethod
    def create(self, name:str, description:str,
             promt:str, creator:str) -> Promt:
        ...

    @abstractmethod
    def delete(self,name:str) -> None:
        ...

    @abstractmethod
    def update(self, old_name: str, name:str, descrition:str,
                promt:str, creator:str) -> Promt:
        ...

# read
    @abstractmethod
    def list_promt(self) -> List[Promt]:
        ...

    @abstractmethod
    def get_promt_by_id(self, name:str) -> Promt:
        ...
    

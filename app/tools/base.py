from abc import ABC, abstractmethod


class EVTool(ABC):
    
    @property
    @abstractmethod
    
    def name(self) ->str :
        pass
    
    @property
    @abstractmethod
    
    def description(self) -> str:
        pass
    
    @abstractmethod
    def execute(self, **kwargs):
        pass
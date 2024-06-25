from abc import ABC, abstractmethod

class IPrint(ABC):
    
    @abstractmethod
    def print(self,path,tipo):
        raise NotImplementedError
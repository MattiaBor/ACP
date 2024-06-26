from abc import ABC,abstractcmethod

class IService(ABC):

    @abstractcmethod
    def Service(self,msg):
        raise NotImplementedError

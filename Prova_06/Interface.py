from abc import ABC, abstractmethod

class IPrinter(ABC):

    @abstractmethod
    def print(self, path, tipo):
        pass
        
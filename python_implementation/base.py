from abc import ABC, ABCMeta, abstractmethod


class Problema(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, n: int) -> None:
        self.n = n

    @abstractmethod
    def solv(self):
        raise NotImplementedError("Falta implementar")

    def __str__(self) -> str:
        return f"Problema de {self.__class__.__name__} com valor {self.n}"

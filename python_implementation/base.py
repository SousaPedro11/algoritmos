from abc import ABC, ABCMeta, abstractmethod


class Problema(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, n: int) -> None:
        self.n = n

    @abstractmethod
    def solv(self):
        raise NotImplementedError('Falta implementar')

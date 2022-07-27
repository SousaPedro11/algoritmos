from python_implementation.base import Problema


class CapSeisUm(Problema):
    def __init__(self) -> None:
        self.n = None

    def solv(self):
        try:
            self.n = int(input("Informe um valor inteiro: "))
            print(f"\nAntecessor de {self.n}: {self.n - 1}")
            return self.n - 1
        except ValueError as e:
            print(e)
            raise e

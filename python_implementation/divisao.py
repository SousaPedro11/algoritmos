from python_implementation.base import Problema


class Divisao(Problema):
    def __init__(self) -> None:
        self.num1 = None
        self.num2 = None

    def solv(self):
        try:
            self.num1 = int(input("Informe um valor inteiro: "))
            self.num2 = int(input("Informe um valor inteiro: "))
            divisao = self.num1 / self.num2
            print(f"\nDivisão de {self.num1} por {self.num2}: {divisao}")
            return divisao
        except ZeroDivisionError as e:
            print(e)
            raise e

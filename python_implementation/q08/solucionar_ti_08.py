"""
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 08
Descriçao do problema:
    Faça uma função que informe a quantidade de dígitos de um número
    inteiro informado pelo usuário. Importante: A entrada de dados
    deve ser int e você não pode converter este valor para string
    no seu programa.
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
"""


class Numero:
    def solv(self):
        """
        Método que soluciona o problema
        """
        try:
            numero = self.ler_numero()
            print(f"O numero {numero} possui {self.digitos_numero(numero)} digitos.")
        except ValueError as e:
            print(e)

    def digitos_numero(self, numero) -> int:
        count = 0
        while numero != 0:
            numero //= 10
            count += 1
        return count

    def ler_numero(self) -> int:
        numero = None
        while True:
            try:
                numero = int(input("Numero inteiro: "))
                break
            except ValueError:
                continue
        return numero


if __name__ == "__main__":
    Numero().solv()

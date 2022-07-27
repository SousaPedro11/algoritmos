"""
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 04
Descriçao do problema:
    Faça um Programa que peça os dados de 5 pessoas(nome, idade e altura),
    armazene cada informação utilizando estrutura de lista e dicionários. Imprima nome,
    a idade e a altura de cada pessoa, ordenando de acordo com a idade, da pessoa mais nova
    para a mais velha. Para pessoas menores que 18 anos deve ser adicionada a
    observação ‘menor de idade’.
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama o de leitura de dados de acordo com qte_pessoas, no caso 5,
    e depois chama o método de impressão em tela

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
"""


class Pessoas:
    def __init__(self, qte_pessoas: int = 5):
        self.qte_pessoas = qte_pessoas
        self.pessoas: list = []

    def solv(self) -> list:
        """
        Método que soluciona o problema

        Returns:
            int: Anos para populacao A >= populacao B
        """
        try:
            for i in range(self.qte_pessoas):
                self.adiciona_pessoa(self.ler_pessoa(i + 1))
            self.imprime_pessoas(self.pessoas)
            return self.pessoas
        except ValueError as e:
            print(e)

    def ler_pessoa(self, index) -> dict:
        pessoa = {}
        nome = ""
        idade = -1
        altura = -1
        print(f"\nPessoa {index}")
        while len(nome) < 4:
            nome = input("Informe o nome da pessoa: ")

        while idade < 0:
            try:
                idade = int(input("Informe a idade: "))
            except ValueError:
                continue

        while not 0.30 < altura <= 3.0:
            try:
                altura = float(input("Informe a altura: "))
            except ValueError:
                continue

        pessoa["nome"] = nome
        pessoa["idade"] = idade
        pessoa["altura"] = altura

        return pessoa

    def adiciona_pessoa(self, pessoa: dict) -> None:
        self.pessoas.append(pessoa)

    @property
    def pessoas(self):
        return self._pessoas

    @pessoas.setter
    def pessoas(self, lista: list):
        self._pessoas = lista

    def imprime_pessoas(self, pessoas: list) -> None:
        pessoas = self.ordena_por_idade(pessoas)
        for p in pessoas:
            print()
            print(f'Nome: {p.get("nome")}')
            print(f'Idade: {p.get("idade")}')
            print(f'Altura: {p.get("altura")}')
            if p.get("idade") < 18:
                print("OBS: menor de idade")

    def ordena_por_idade(self, pessoas: list) -> list:
        return sorted(pessoas, key=lambda i: i["idade"])


if __name__ == "__main__":
    Pessoas().solv()

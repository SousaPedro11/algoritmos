'''
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 08
Descriçao do problema:
    Nome na vertical. Faça um programa que solicite o nome do usuário
    e imprima-o na vertical, em formato de escada, conforme exemplo
    abaixo (para a entrada "JOSE"):
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
'''


class Numero:

    def solv(self):
        """
        Método que soluciona o problema
        """
        try:
            nome = input('Nome: ')
            for i in range(1, len(nome) + 1):
                print(nome[:i])
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    Numero().solv()

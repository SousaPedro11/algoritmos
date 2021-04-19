'''
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 12
Descriçao do problema:
    Utilizando o módulo re, fazer uma função que retorne a "string limpa", ou seja,
    retire qualquer caracter especial, deixando somente letras (A-Z, a-z), números (0-9) e espaço (" ").
A função receberá um string e retornara uma "string limpa", ou seja, após retirar os caracteres inválidos. Exemplos
IN: "2021-03-01T11:37:30";   OUT: "20210301113730"
IN: "Jose Maria. -61";   OUT: "Jose Maria 61"

Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
'''
import re


class StringSelecionar:

    def solv(self, date_str: str):
        """
        Método que soluciona o problema
        """
        try:
            data = self.validar_string(date_str)
            print(data)
        except ValueError as e:
            print(e)

    def validar_string(self, string):
        string = re.sub("[^0-9a-zA-Z ]", "", string)

        return string


if __name__ == '__main__':
    StringSelecionar().solv('2021-03-01T11:37:30')
    StringSelecionar().solv('Jose Maria. -61')
    StringSelecionar().solv('17MAR:2348')

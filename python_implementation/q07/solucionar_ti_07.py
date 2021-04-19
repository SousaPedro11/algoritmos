'''
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 07
Descriçao do problema:
    Data com mês por extenso. Construa uma função que receba uma
    data no formato DD/MM/AAAA e devolva uma string no formato
    "DD de mesPorExtenso de AAAA". Opcionalmente, valide a data e
    retorne NULL caso a data seja inválida. DD=dia com dois
    dígitos sempre, mesPorExtenso é o nome do mês (Janeiro,
    Fevereiro, …) e AAAA é o ano com 4 dígitos.
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
'''
import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


class Alunos:

    def solv(self, date_str: str):
        """
        Método que soluciona o problema
        """
        try:
            data = self.validar_data(date_str)
            print(data)
        except ValueError as e:
            print(e)

    def validar_data(self, date_str):
        try:
            data = datetime.strptime(date_str, '%d/%m/%Y').strftime("%d de %B de %Y")
        except ValueError:
            return 'NULL'
        return data


if __name__ == '__main__':
    Alunos().solv('17/03/2021')
    Alunos().solv('17/00/2021')

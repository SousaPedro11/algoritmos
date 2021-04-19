'''
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 11
Descriçao do problema:
    Validar padrão da string no formato "DDMMM:HHmm":
Sendo:
  "DD"   dia **
  "MMM"  abreviação do mês por extenso, US, uppercase (Exemplo Jan Feb Mar Apr May...)
  ":"    Separador Fixo
  "HH"   Horas **
  "mm"   Minutos **

** Dia, hora e minutos sempre com 2 dígitos

A função deve receber uma string qualquer e validar se ela atende ao padrão descrito acima e retornar verdadeiro, ou caso não atenda, retornar falso.
Exemplo:   s = '06MAY:1700' -> True
Exemplo:   s = '06/05:1700' -> False

Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
'''

from datetime import datetime


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
            datetime.strptime(date_str.lower(), '%d%b:%H%M')
        except ValueError:
            return False
        return True


if __name__ == '__main__':
    Alunos().solv('06MAY:1700')
    Alunos().solv('06/05:1700')
    Alunos().solv('17MAR:2348')

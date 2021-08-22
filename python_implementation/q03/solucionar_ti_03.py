'''
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 01
Descriçao do problema:
    Sabendo que a população de um país A é de 88167 habitantes com uma taxa anual de
    crescimento de 3% e a população do país B é de 199561 habitantes com uma taxa de
    crescimento de 1.5%, faça um programa que calcule e escreva o número de anos necessários
    para que a população do país A ultrapasse ou iguale a população do país B, considerando
    que serão mantidas as taxas de crescimento.
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de populacao e taxa
    O método solv() calcula a o montante de cada populacao e incrementa o ano
    até o montante A >= montante B

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
'''


class CrescimentoPopulacional:

    def __init__(self, populacao_a: float = 88167, populacao_b: float = 199561, taxa_a: float = 3, taxa_b: float = 1.5):
        self.populacao_a = populacao_a
        self.populacao_b = populacao_b
        self.taxa_a = taxa_a / 100
        self.taxa_b = taxa_b / 100

    def solv(self) -> int:
        """
        Método que soluciona o problema

        Returns:
            int: Anos para populacao A >= populacao B
        """
        try:
            anos = 0
            while self.populacao_a < self.populacao_b:
                self.populacao_a += (self.populacao_a * self.taxa_a)
                self.populacao_b += (self.populacao_b * self.taxa_b)
                anos += 1
            print(anos)
            return anos
        except ValueError as e:
            print(e)


class TestPopulacao:

    def test_padrao(self):
        output = CrescimentoPopulacional().solv()
        assert output == 56

    def test_A90M_B200M(self):
        output = CrescimentoPopulacional(90000000, 200000000).solv()
        assert output == 55

    def test_A_maior_que_B(self):
        output = CrescimentoPopulacional(50, 10).solv()
        assert output == 0


if __name__ == '__main__':
    CrescimentoPopulacional().solv()

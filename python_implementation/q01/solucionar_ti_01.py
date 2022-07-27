from io import StringIO

"""
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 01
Descriçao do problema:
    Faça um programa para a leitura de duas notas parciais de um aluno.
    O programa deve calcular a média alcançada por aluno e apresentar:
    • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    • A mensagem "Reprovado", se a média for menor do que sete;
    • A mensagem "Aprovado com Distinção", se a média for maior ou igual a dez.
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    Os passos são:
    - Ler notas
    - Calcula Média
    - Retorna Resultado Final
Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
"""


class MediaAluno:
    def __init__(self, qte_notas: int = 2) -> None:
        """
        Construtor de classe que define a quantidade de notas com um optional

        Args:
            qte_notas (int, optional): Quantidade de notas. Defaults to 2.
        """
        self.num_notas = qte_notas

    def solv(self) -> str:
        """
        Método que soluciona o problema

        Returns:
            str: Resultado da média final ('Reprovado, 'Aprovado' ou 'Aprovado com Distincao).
        """
        try:
            media = self._calcula_media(self._ler_notas(self.num_notas))
            resultado = self._obtem_resultado(media)
            print(resultado)
            return resultado
        except ValueError as e:
            print(e)

    def _ler_notas(self, num_notas: int) -> list:
        """
        Método que lê as notas

        Args:
            num_notas (int): Número de notas a serem lidas

        Returns:
            list: Lista de notas
        """
        notas = []
        for i in range(1, num_notas + 1):
            nota = -1
            while nota < 0:
                nota = float(input(f"Informe a nota {i}: "))
                notas.append(nota)
        return notas

    def _calcula_media(self, notas: list) -> float:
        """
        Calcula a média a partir de uma lista de notas

        Args:
            notas (list): Notas do aluno

        Returns:
            float: Média do aluno
        """
        media = sum(notas) / len(notas)
        return media

    def _obtem_resultado(self, media: float):
        """
        Retorna o resultado a partir da média calculada

        Args:
            media (float): Média calculada

        Returns:
            str: Resultado Final
        """
        if media < 7:
            return "Reprovado"
        elif media >= 7 and media < 10:
            return "Aprovado"
        return "Aprovado com Distinção"


class TestMedia:
    def ler(self, monkeypatch, a, b):
        monkeypatch.setattr("sys.stdin", StringIO(f"{a}\n{b}\n"))

    def test_reprovado(self, monkeypatch):
        self.ler(monkeypatch, 6.9, 7)
        output = MediaAluno().solv()
        assert output == "Reprovado"

    def test_aprovado(self, monkeypatch):
        self.ler(monkeypatch, 7, 7)
        output = MediaAluno().solv()
        assert output == "Aprovado"

    def test_aprovado_dinstincao_1(self, monkeypatch):
        self.ler(monkeypatch, 13, 7)
        output = MediaAluno().solv()
        assert output == "Aprovado com Distinção"

    def test_aprovado_dinstincao_2(self, monkeypatch):
        self.ler(monkeypatch, 15, 7)
        output = MediaAluno().solv()
        assert output == "Aprovado com Distinção"


if __name__ == "__main__":
    MediaAluno().solv()

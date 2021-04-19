from python_implementation.solucionar_ti import MediaAluno
from io import StringIO


class TestMedia:
    def ler(self, monkeypatch, a, b):
        monkeypatch.setattr('sys.stdin', StringIO(f'{a}\n{b}\n'))

    def test_reprovado(self, monkeypatch):
        self.ler(monkeypatch, 6.9, 7)
        output = MediaAluno().solv()
        assert output == 'Reprovado'

    def test_aprovado(self, monkeypatch):
        self.ler(monkeypatch, 7, 7)
        output = MediaAluno().solv()
        assert output == 'Aprovado'

    def test_aprovado_dinstincao_1(self, monkeypatch):
        self.ler(monkeypatch, 13, 7)
        output = MediaAluno().solv()
        assert output == 'Aprovado com Distinção'

    def test_aprovado_dinstincao_2(self, monkeypatch):
        self.ler(monkeypatch, 15, 7)
        output = MediaAluno().solv()
        assert output == 'Aprovado com Distinção'

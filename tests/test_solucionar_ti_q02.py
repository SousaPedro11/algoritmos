from io import StringIO

import pytest

from python_implementation.q02.solucionar_ti_02 import LerDados


class TestDados:
    def ler(self, monkeypatch, valores):
        valores = "\n".join(valores)
        monkeypatch.setattr("sys.stdin", StringIO(valores))

    def test_valido(self, monkeypatch):
        dados = ["Pedro Sousa", "28", "4000.00", "m", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_nome_dois_char(self, monkeypatch):
        dados = ["pe", "Pedro Sousa", "28", "4000.00", "m", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_idade_negativa(self, monkeypatch):
        dados = ["Pedro Sousa", "-5", "28", "4000.00", "m", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_idade_nula(self, monkeypatch):
        dados = ["Pedro Sousa", "0", "28", "4000.00", "m", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_idade_150(self, monkeypatch):
        dados = ["Pedro Sousa", "150", "28", "4000.00", "m", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_salario_negativo(self, monkeypatch):
        dados = ["Pedro Sousa", "28", "-1", "4000.00", "m", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_sexo_invalido(self, monkeypatch):
        dados = ["Pedro Sousa", "28", "4000.00", "b", "m", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_estado_civil_invalido(self, monkeypatch):
        dados = ["Pedro Sousa", "150", "28", "4000.00", "m", "a", "c"]
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_salario_string(self, monkeypatch):
        dados = ["Pedro Sousa", "28", "salario", "m", "c", "a"]
        self.ler(monkeypatch, dados)

        with pytest.raises(ValueError):
            output = LerDados().solv()
            esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
            assert output == esperado

    def test_idade_string(self, monkeypatch):
        dados = ["Pedro Sousa", "idade", "4000.00", "m", "c", "a"]
        self.ler(monkeypatch, dados)

        with pytest.raises(ValueError):
            output = LerDados().solv()
            esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
            assert output == esperado

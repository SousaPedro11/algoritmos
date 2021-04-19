from io import StringIO

'''
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 01
Descriçao do problema:
    Faça um programa que leia e valide os dados abaixo.
    O programa só deve terminar, mostrando a mensagem de ‘dados lidos com sucesso’,
    quando todos os dados forem informados corretamente.
        a. Nome: maior que 3 caracteres;
        b. Idade: entre 0 e 150;
        c. Salário: maior que zero;
        d. Sexo: 'f' ou 'm';
        e. Estado Civil: 's', 'c', 'v', ou 'd';
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    No método solv() é chamado cada método para inicializar as variaveis e depois outro
    que retorna um objeto Pessoa. O solv retorna a representação de Pessoa e imprime ('dados lidos com sucesso')

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
'''


class Pessoa:
    def __init__(self, nome: str, idade: int, salario: float, sexo: str, e_civil: str):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.sexo = sexo
        self.estado_civil = e_civil

    def __str__(self):
        return f'Nome: {self.nome}\n' \
               f'Idade: {self.idade}\n' \
               f'Salário: {self.salario}\n' \
               f'Sexo: {self.sexo}\n' \
               f'Estado Civil: {self.estado_civil}\n'


class LerDados:
    SEXO = {
        'f': 'Feminino',
        'm': 'Masculino'
    }
    CIVIL = {
        's': 'Separado',
        'c': 'Casado',
        'v': 'Viúvo',
        'd': 'Divorciado'
    }

    def solv(self) -> str:
        """
        Método que soluciona o problema

        Returns:
            str: Representacao de Pessoa
        """
        try:
            nome = self._ler_nome()
            idade = self._ler_idade()
            salario = self._ler_salario()
            sexo = self._ler_sexo()
            e_civil = self._ler_estado_civil()
            resultado = self._obtem_resultado(
                nome, idade, salario, sexo, e_civil)
            print('dados lidos com sucesso')
            return resultado.__str__()
        except ValueError as e:
            print(e)

    def _ler_nome(self) -> str:
        nome: str = ''
        while len(nome) < 4:
            nome = input("Informe um nome ('mais de 3 caracteres'): ")
        return nome

    def _ler_idade(self) -> int:
        idade = -1
        while not 0 < idade < 150:
            try:
                idade = int(input("Informe a idade (entre 0 e 150 anos): "))
            except ValueError:
                continue
        return idade

    def _ler_salario(self) -> float:
        salario = 0.0
        while salario <= 0:
            try:
                salario = float(input("Informe o salário (maior que 0): "))
            except ValueError:
                continue
        return salario

    def _ler_sexo(self) -> str:
        sexo = 'a'
        while sexo not in self.SEXO.keys():
            sexo = input("Informe o sexo ('f' ou 'm'): ")
        return self.SEXO.get(sexo)

    def _ler_estado_civil(self) -> str:
        e_civil = 'a'
        while e_civil not in self.CIVIL.keys():
            e_civil = input("Informe o estado civil ('s', 'c', 'v', ou 'd'): ")
        return self.CIVIL.get(e_civil)

    def _obtem_resultado(self, nome, idade, salario, sexo, e_civil) -> Pessoa:
        pessoa = Pessoa(nome, idade, salario, sexo, e_civil)
        return pessoa


class TestMedia:
    def ler(self, monkeypatch, valores):
        valores = '\n'.join(valores)
        monkeypatch.setattr('sys.stdin', StringIO(valores))

    def test_valido(self, monkeypatch):
        dados = ['Pedro Sousa', '28', '4000.00', 'm', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_nome_dois_char(self, monkeypatch):
        dados = ['pe', 'Pedro Sousa', '28', '4000.00', 'm', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_idade_negativa(self, monkeypatch):
        dados = ['Pedro Sousa', '-5', '28', '4000.00', 'm', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_idade_nula(self, monkeypatch):
        dados = ['Pedro Sousa', '0', '28', '4000.00', 'm', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_idade_150(self, monkeypatch):
        dados = ['Pedro Sousa', '150', '28', '4000.00', 'm', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_salario_negativo(self, monkeypatch):
        dados = ['Pedro Sousa', '28', '-1', '4000.00', 'm', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_sexo_invalido(self, monkeypatch):
        dados = ['Pedro Sousa', '28', '4000.00', 'b', 'm', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado

    def test_estado_civil_invalido(self, monkeypatch):
        dados = ['Pedro Sousa', '150', '28', '4000.00', 'm', 'a', 'c']
        self.ler(monkeypatch, dados)
        output = LerDados().solv()
        esperado = "Nome: Pedro Sousa\nIdade: 28\nSalário: 4000.0\nSexo: Masculino\nEstado Civil: Casado\n"
        assert output == esperado


if __name__ == '__main__':
    LerDados().solv()

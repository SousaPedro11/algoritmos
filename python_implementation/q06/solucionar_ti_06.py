"""
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 06
Descriçao do problema:
    Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
    quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
    Implemente a entrada de dados em formato csv, de modo que se possa fazer a entrada de dados
    em lote e não de forma unitária.
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
"""


class Alunos:
    def solv(self):
        """
        Método que soluciona o problema
        """
        try:
            caminho = "alunos.csv"
            alunos = self.popula_alunos(self.ler_csv(caminho))
            self.mostra_alunos_13_menor_media(alunos)
        except ValueError as e:
            print(e)

    def ler_csv(self, path: str):
        with open(path, "r") as f:
            registros = f.readlines()
        return registros

    def is_number(self, a, b):
        try:
            int(a)
            float(b)
            return True
        except ValueError:
            return False

    def popula_alunos(self, registros):
        alunos = []
        for r in registros:
            idade, altura = r.split(";")
            idade, altura = idade.strip(), altura.strip()
            if self.is_number(idade, altura):
                idade, altura = int(idade), float(altura)
                alunos.append({"idade": idade, "altura": altura})
        return alunos

    def calcula_media_alturas(self, alunos):
        alturas = [a["altura"] for a in alunos]
        media_altura = sum(alturas) / len(alturas)
        return media_altura

    def mostra_alunos_13_menor_media(self, alunos):
        count = 0
        media_altura = self.calcula_media_alturas(alunos)
        for a in alunos:
            if a["idade"] > 13 and a["altura"] < media_altura:
                print(a)
                count += 1
        print(f"Média altura: {media_altura}")
        print(f"Quantidade alunos > 13 anos e altura abaixo da média: {count}")


if __name__ == "__main__":
    Alunos().solv()

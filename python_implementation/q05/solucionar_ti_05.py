'''
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 05
Descriçao do problema:
    Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
    encerrando a entrada de dados quando for informado um valor igual a -1
    (que não deve ser armazenado). Após esta entrada de dados, faça:
    a. Mostre a quantidade de valores que foram lidos;
    b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d. Calcule e mostre a soma dos valores;
    e. Calcule e mostre a média dos valores;
    f. Calcule e mostre a quantidade de valores acima da média calculada;
    g. Calcule e mostre a quantidade de valores abaixo de sete;
    h. Encerre o programa com uma mensagem;
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
'''


class Notas:

    def __init__(self):
        self.notas: list = []

    def solv(self) -> list:
        """
        Método que soluciona o problema
        """
        try:
            self.ler_notas()
            print()
            print(f'Numero de valores lidos: {len(self.notas)}')
            print('Valores na ordem de leitura: ')
            print(', '.join(str(x) for x in self.notas))
            print('Valores na ordem inversa:')
            for e in self.notas[::-1]:
                print(e)
            print(f'Soma dos valores: {sum(self.notas)}')
            media = self.media_notas()
            print(f'Média notas: {media}')
            print(f'Quantidade acima da média: {self.qte_acima_media(media)}')
            print(f'Quantidade abaixo de 7: {self.abaixo_sete()}')
            print('\nFim de execução')
            return self.notas
        except ValueError as e:
            print(e)

    def ler_notas(self):
        count = 0
        while True:
            count += 1
            nota = float(input(f'Nota (0 a 10) {count}: '))
            if nota == -1 and len(self.notas) == 0:
                print('insira ao menos um valor')
                continue
            elif nota == -1:
                break
            elif not 0 <= nota <= 10:
                print('nota não contabilizada (somente de 0 a 10)')
                continue
            else:
                self.notas.append(nota)

    def media_notas(self) -> float:
        return sum(self.notas) / len(self.notas)

    def qte_acima_media(self, media: float) -> int:
        count = 0
        for num in self.notas:
            if num > media:
                count += 1
        return count

    @property
    def notas(self) -> list:
        return self._notas

    @notas.setter
    def notas(self, lista: list):
        self._notas = lista

    def abaixo_sete(self) -> int:
        count = 0
        for i in self.notas:
            if i < 7:
                count += 1
        return count


if __name__ == '__main__':
    Notas().solv()

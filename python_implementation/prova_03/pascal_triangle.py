def binomial(row: int, column: int):
    """
    Calcula o coeficiente binomial correspondente ao triangulo Pascal
    :param row: numeradores do binomio
    :param column: denominadores do binomio
    :return: coeficiente calculado
    """
    # linha (numerador) ou coluna (denominador) não podem ser negativos
    if row < 0 or column < 0:
        raise ValueError('Não pode ser negativo!')
    # denominador deve ser de 0 ao valor do numerador
    if not 0 <= column <= row:
        raise ValueError(f'Deve ser de 0 a {row}')
    # inicializa o coeficiente
    coef = 1
    # varre de 0 ao minimo entre denominador e (numerador - denominador)
    for t in range(min(column, row - column)):
        # coeficiente assume o valor variavel entre as posicoes
        coef *= row
        # divide pelo elemento do range + 1
        coef /= t + 1
        # decrementa a linha
        row -= 1
    return int(coef)


def pascal_triangle(limit: int):
    """
    Monta a estrutura do triangulo usando lista de listas com tamanhos variaveis
    :param limit: numero de linhas a serem construidas
    :return: lista de linhas do Triangulo representadas por listas com os coeficientes binomiais
    """
    # list comprehension que monta a estrutura
    lista = [[binomial(x, y) for y in range(x + 1)] for x in range(limit)]
    return lista


def print_pascal_triangle(data: list):
    """
    Imprime o triangulo de pascal na tela
    :param data: lista de linhas do triangulo
    :return: None
    """
    # percorre as linhas
    for e in data:
        # descompacta os elementos de cada linha com um espaco entre eles
        print(*e, sep=' ')


def print_sum_each_row(data: list):
    """
    Imprime a soma dos coeficientes de cada linha. Equivalente a 2**(indice_linha) - indice vai de 0 a n_linhas-1.
    :param data: lista de linhas do triangulo
    :return: None
    """
    # list comprehension para imprimir a soma de elementos de cada linha
    [print(sum(e)) for e in data]


def solucao():
    """
    Metodo que segue o passo a passo para solucionar a questao
    :return: None
    """
    # monta a matriz de valores
    pascal = pascal_triangle(6)
    print('TRIANGULO DE PASCAL')
    # imprime triangulo de pascal
    print_pascal_triangle(pascal)
    print('\nSOMA DOS COEFICIENTES')
    # calcula soma dos elementos de cada linha
    print_sum_each_row(pascal)


if __name__ == '__main__':
    solucao()

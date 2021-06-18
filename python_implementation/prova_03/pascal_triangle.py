def binomial(row: int, column: int):
    if row < 0 or column < 0:
        raise ValueError('Não pode ser negativo!')
    if not 0 <= column <= row:
        raise ValueError(f'Deve ser de 0 a {row}')
    b = 1
    for t in range(min(column, row - column)):
        b *= row
        b /= t + 1
        row -= 1
    return int(b)


def pascal_triangle(limit: int):
    lista = [[binomial(x, y) for y in range(x + 1)] for x in range(limit)]
    return lista


def print_pascal_triangle(matrix: list):
    for e in matrix:
        print(*e, sep=' ')


def print_sum_each_row(matrix: list):
    values = [print(sum(e)) for e in matrix]
    return values


def solucao():
    # monta a matriz de valores
    pascal = pascal_triangle(10)
    print('TRIANGULO DE PASCAL')
    # imprime triangulo de pascal
    print_pascal_triangle(pascal)
    print('\nSOMA DOS ELEMENTOS')
    # calcula soma dos elementos de cada linha
    print_sum_each_row(pascal)


if __name__ == '__main__':
    solucao()

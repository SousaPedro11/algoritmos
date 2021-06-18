import random
from typing import List
import numpy as np
from scipy import sparse


def __imprime_matriz(matriz: List[List]) -> None:
    try:
        print(f'Matriz de tamanho: {len(matriz)}')
        for linha in matriz:
            print('  '.join(str(x) for x in linha))
        print('\n')
    except ValueError as e:
        print(e)


def __define_matriz(tamanho: int) -> List[List]:
    """
    Metodo de definicao da matriz.

    :return:
    """
    _matriz = __cria_matriz_quadrada(tamanho)
    return _matriz


def __sparse_elements(ordem: int, percent: int = 20):
    """
    Cria a matriz esparsa os elementos nao nulos da matriz esparsa
    :param ordem: Ordem da matriz
    :param percent: Percentual inteiro de nao nulos
    :return: Matriz em estrutura de lista de listas
    """
    _length = round(ordem**2 * percent / 100)
    values = np.random.randint(low=1, high=9, size=_length)
    rows = np.random.randint(low=0, high=ordem, size=_length)
    columns = np.random.randint(low=0, high=ordem, size=_length)
    # falta ajustar
    cords = np.array(set(zip(rows, columns)))
    print(values.size, rows.size, columns.size, cords.size)
    while len(cords) < _length:
        cords.ap((random.randrange(ordem), random.randrange(ordem)))
    _sparse = [[t[0], t[1], v] for t, v in zip(cords, values)]
    return _sparse


def __cria_matriz_quadrada(tamanho: int, sparse_elements: List[List] = None):
    """
    Metodo que cria a matriz recursivamente seguindo um padrao de letras por quadrante.

    :param tamanho: Ordem da matriz
    :param i: Linha da matriz
    :return: Matriz preenchida
    """
    _matriz = []
    for _ in range(tamanho):
        _linha = [0 for _ in range(tamanho)]
        _matriz.append(_linha)

    if sparse_elements:
        for cord in sparse_elements:
            _matriz[cord[0]][cord[1]] = cord[2]

    return _matriz


def solucao_problema():
    ordem_matriz = 10000
    _sparse_elements = __sparse_elements(ordem_matriz, 20)
    _matrix = __cria_matriz_quadrada(ordem_matriz, _sparse_elements)
    __imprime_matriz(_matrix)


if __name__ == '__main__':
    solucao_problema()
    # N1 = 10000000  # 1e8
    # N2 = 5000
    # rows = np.arange(N1)
    # cols = (np.floor(np.random.permutation(N1) / float(N1) * N2)).astype(int)
    # w = np.ones(N1)
    # conn_matrix = sparse.csr_matrix((w, (rows, cols)), shape=(N1, N2), dtype=int)
    # print(conn_matrix)

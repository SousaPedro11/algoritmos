import os.path
import random
from typing import List

import numpy as np


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

    :return: Matriz em forma de lista
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
    _length = round(ordem ** 2 * percent / 100)
    values = list(np.random.randint(low=1, high=9, size=_length))
    rows = list(np.random.randint(low=0, high=ordem, size=_length))
    columns = list(np.random.randint(low=0, high=ordem, size=_length))

    cords = set(zip(rows, columns))
    while len(cords) < _length:
        cords.add((random.randrange(ordem), random.randrange(ordem)))
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


def salva_arquivo(element: List, name: str):
    """
    Salva o arquivo com cada valor da lista em uma linha
    :param element: Lista de elementos
    :param name: Nome do arquivo
    :return: None
    """
    with open(name, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(str(x) for x in element))


def imprime_comparativos_arquivo(name_arq_1: str, name_arq_2: str):
    """
    Compara quantos % um arquivo e maior que outro
    :param name_arq_1:
    :param name_arq_2:
    :return: None
    """
    try:
        size_file_1 = os.path.getsize(name_arq_1)
        size_file_2 = os.path.getsize(name_arq_2)
        comparativo = 100 - (min(size_file_1, size_file_2) * 100 / max(size_file_1, size_file_2))
        print(f'Arquivo maior é {comparativo}% maior que o outro')
    except Exception as e:
        print(e.__str__())


def atualiza_matriz(matrix: List[List], sparce: List[List]):
    """
    Atualiza os elementos de uma matriz a partir de uma lista de coordenadas-valor
    :param matrix: Matriz a ser atualizada
    :param sparce: Lista da coordenada-valor
    :return: Matriz atualizada
    """
    if sparce:
        for cord in sparce:
            matrix[cord[0]][cord[1]] = cord[2]

    return matrix


def solucao_problema():
    # questao a, b, c e d
    # define ordem da matriz
    ordem_matriz = 10000
    # cria lista de elementos nao nulos de uma matriz esparsa
    _sparse_elements = __sparse_elements(ordem_matriz, 20)
    # cria matriz esparsa a partir da lista de elementos
    _matrix = __cria_matriz_quadrada(ordem_matriz, _sparse_elements)
    # define nome dos arquivos
    filename_matrix = 'arquivoA.txt'
    filename_sparse_elements = 'arquivoB.txt'
    # salva matriz e lista de elementos nos respectivos arquivos
    salva_arquivo(_matrix, filename_matrix)
    salva_arquivo(_sparse_elements, filename_sparse_elements)
    # imprime o comparativo dos tamanhos dos arquivos mostrando quantos % é maior
    imprime_comparativos_arquivo(filename_matrix, filename_sparse_elements)
    # define uma outra lista
    _sparse_elements_2 = __sparse_elements(ordem_matriz, 10)
    # atualiza a matriz a partir da segunda lista
    _matrix = atualiza_matriz(_matrix, _sparse_elements_2)
    # salva a matriz atualizada
    salva_arquivo(_matrix, 'arquivoC.txt')


if __name__ == '__main__':
    solucao_problema()

import math


def __cria_matriz_quadrada(tamanho=20):
    matriz = []
    for _ in range(tamanho):
        linha = ['0' for _ in range(tamanho)]
        matriz.append(linha)
    return matriz


def __diagonais(matriz):
    tamanho = len(matriz)
    diagonal_principal: list = []
    diagonal_secundaria: list = []
    top, bottom, right, left = 'B', 'A', 'Y', 'X'
    if tamanho >= 20:
        ponto_medio = math.ceil(tamanho / 2)
        diagonal_principal = [j for j in range(tamanho)]
        diagonal_secundaria = [j for j in range(tamanho)[::-1]]

        for i, j in enumerate(diagonal_secundaria):
            matriz[i][j] = right if (i < ponto_medio) else left
        for i, j in enumerate(diagonal_principal):
            matriz[i][j] = top if (j < ponto_medio) else bottom
    return diagonal_principal, diagonal_secundaria


def __quadrantes(matriz, diagonal_p, diagonal_s):
    tamanho = len(matriz)
    if tamanho >= 20:
        for i in range(tamanho):
            elemento_dp = diagonal_p[i]
            elemento_ds = diagonal_s[i]
            for j in range(tamanho):
                if elemento_dp < j < elemento_ds:
                    matriz[i][j] = 'B'
                elif elemento_ds < j < elemento_dp:
                    matriz[i][j] = 'A'
                elif j < elemento_dp and j < elemento_ds:
                    matriz[i][j] = 'X'
                elif j > elemento_dp and j > elemento_ds:
                    matriz[i][j] = 'Y'


def __imprime_matriz(matriz):
    try:
        print(f'matriz de tamanho: {len(matriz)}')
        for linha in matriz:
            print('  '.join(linha))
        print('\n')
    except ValueError as e:
        print(e)


def __define_tamanho(msg: str):
    while True:
        try:
            tamanho = int(input(f'{msg}: '))
            break
        except ValueError:
            print('O valor informado não é um inteiro!')
    return tamanho


def __define_matriz_maior():
    print('MATRIZ MAIOR')
    tamanho = __define_tamanho(
        msg='Defina a ordem de uma matriz quadrada (inteiro maior ou igual a 20)',
    )
    while tamanho < 20:
        print('Valor informado menor que 20!')
        tamanho = __define_tamanho(
            msg='Defina a ordem de uma matriz quadrada (inteiro maior ou igual a 20)',
        )
    matriz = __cria_matriz_quadrada(tamanho)
    diagonal_principal, diagonal_secundaria = __diagonais(matriz)
    __quadrantes(matriz, diagonal_principal, diagonal_secundaria)
    __imprime_matriz(matriz)
    return matriz


def __define_matriz_menor(len_matriz_maior: int):
    print('MATRIZ MENOR')
    tamanho = __define_tamanho(
        msg=f'Defina a ordem de uma matriz quadrada (inteiro menor que {len_matriz_maior})',
    )
    while tamanho >= len_matriz_maior:
        print(f'Valor informado maior que {len_matriz_maior}!')
        tamanho = __define_tamanho(
            msg='Defina a ordem de uma matriz quadrada (inteiro maior ou igual a 20)',
        )
    matriz = __cria_matriz_quadrada(tamanho)
    __imprime_matriz(matriz)
    return matriz


if __name__ == '__main__':
    matriz_maior = __define_matriz_maior()
    matriz_menor = __define_matriz_menor(len(matriz_maior))

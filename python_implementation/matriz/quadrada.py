import math


def cria_matriz_quadrada(tamanho=20):
    matriz = []
    # FIXME ajustar para 20 apenas
    if tamanho <= 20:
        for _ in range(tamanho):
            linha = ['0' for _ in range(tamanho)]
            matriz.append(linha)
    else:
        raise ValueError('Tamanho deve ser no máximo 20')
    return matriz


def diagonais(matriz):
    tamanho = len(matriz)
    diagonal_principal: list = []
    diagonal_secundaria: list = []
    top, bottom, right, left = 'B', 'A', 'Y', 'X'
    # FIXME ajustar para 20 apenas
    if tamanho <= 20:
        ponto_medio = math.ceil(tamanho / 2)
        diagonal_principal = [j for j in range(tamanho)]
        diagonal_secundaria = [j for j in range(tamanho)[::-1]]

        for i, j in enumerate(diagonal_secundaria):
            matriz[i][j] = right if (i < ponto_medio) else left
        for i, j in enumerate(diagonal_principal):
            matriz[i][j] = top if (j < ponto_medio) else bottom
    return diagonal_principal, diagonal_secundaria


def quadrantes(matriz, diagonal_p, diagonal_s):
    tamanho = len(matriz)
    # FIXME ajustar para 20 apenas
    if tamanho <= 20:
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


def imprime_matriz(matriz):
    try:
        print(f'matriz de tamanho: {len(matriz)}')
        for linha in matriz:
            print('\t'.join(linha))
        print('\n')
    except ValueError as e:
        print(e)


tam = 6
mat = cria_matriz_quadrada(tam)
dp, ds = diagonais(mat)
quadrantes(mat, dp, ds)
imprime_matriz(mat)

tam = 5
mat = cria_matriz_quadrada(tam)
dp, ds = diagonais(mat)
quadrantes(mat, dp, ds)
imprime_matriz(mat)

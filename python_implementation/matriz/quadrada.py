import math


def cria_matriz_quadrada(tamanho):
    ponto_medio = math.ceil(tamanho/2)
    print(ponto_medio)
    matriz = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if i == j and j < ponto_medio:
                linha.append('B')
            elif i == j and j >= ponto_medio:
                linha.append('A')
            elif i == tamanho - 1 - j < ponto_medio:
                linha.append('Y')
            elif i == tamanho - 1 - j >= ponto_medio:
                linha.append('X')
            else:
                linha.append('0')
        matriz.append(linha)
    return matriz


def imprime_matriz(matriz):
    print(f'matriz de tamanho: {len(matriz)}')
    for linha in matriz:
        print('\t'.join(linha))
    print('\n')


tamanho = 6
matriz = cria_matriz_quadrada(tamanho)
imprime_matriz(matriz)

tamanho = 5
matriz = cria_matriz_quadrada(tamanho)
imprime_matriz(matriz)

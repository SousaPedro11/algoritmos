from typing import List

matriz = []


def __imprime_matriz(matriz: List[List[str]]) -> None:
    """
    Imprime a matriz na tela.

    :param matriz: Matriz de entrada
    :return:
    """
    try:
        # print(f'Matriz de tamanho: {len(matriz)}')
        for linha in matriz:
            print('  '.join(linha))
        print('\n')
    except ValueError as e:
        print(e)


def __define_tamanho(msg: str) -> int:
    """
    Verificador da entrada.

    :param msg: Mensagem a ser exibida
    :return:
    """
    while True:
        try:
            tamanho = int(input(f'{msg}: '))
            break
        except ValueError:
            print('O valor informado não é um inteiro!')
    return tamanho


def __define_matriz() -> List[List[str]]:
    """
    Metodo de definicao da matriz.

    :return:
    """
    # print('MATRIZ MAIOR')
    _tamanho = __define_tamanho(
        msg=f'Defina a ordem de uma matriz quadrada (a partir de 10)',
    )
    while _tamanho < 10:
        print(f'Valor informado menor que 10!')
        _tamanho = __define_tamanho(
            msg=f'Defina a ordem de uma matriz quadrada (a partir de 10)',
        )
    _matriz = __cria_matriz_quadrada(_tamanho)
    return _matriz


def __cria_matriz_quadrada(tamanho: int, i: int = 0):
    """
    Metodo que cria a matriz recursivamente seguindo um padrao de letras por quadrante.

    :param tamanho: Ordem da matriz
    :param i: Linha da matriz
    :return: Matriz preenchida
    """
    linha = []
    if i == tamanho:
        return matriz
    else:
        for c in range(tamanho):
            linha.append(' ')
        matriz.append(linha)
        for c in range(tamanho):
            # verifica posicoes
            acima_diagonal_principal = i < c
            acima_diagonal_secundaria = i + c < tamanho
            abaixo_diagonal_secundaria = i + c > tamanho
            abaixo_diagonal_principal = i > c

            if acima_diagonal_principal and acima_diagonal_secundaria:
                matriz[i][c] = 'X'
            elif abaixo_diagonal_principal and acima_diagonal_secundaria:
                matriz[i][c] = 'B'
            elif acima_diagonal_principal and abaixo_diagonal_secundaria:
                matriz[i][c] = 'A'
            elif abaixo_diagonal_principal and abaixo_diagonal_secundaria:
                matriz[i][c] = 'Y'
        return __cria_matriz_quadrada(tamanho, i + 1)


def solucao_problema():
    matriz_maior = __define_matriz()
    __imprime_matriz(matriz_maior)


if __name__ == '__main__':
    solucao_problema()

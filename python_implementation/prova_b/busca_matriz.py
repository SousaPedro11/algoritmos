import random
import string
from typing import List

lista = string.ascii_lowercase[:10]
options = random.sample(lista, 4)
cordinates = []


def __cria_matriz_quadrada(tamanho: int = 20) -> List[List[str]]:
    """
    Metodo que cria uma matriz quadrada a partir da lista de 4 letras.

    :param tamanho: Ordem da matriz quadrada a ser criada
    :return: Matriz criada
    """
    matriz = []
    for _ in range(tamanho):
        linha = [random.choice(options) for _ in range(tamanho)]
        matriz.append(linha)
    return matriz


def __imprime_matriz(matriz: List[List[str]]) -> None:
    """
    Imprime a matriz na tela.

    :param matriz: Matriz de entrada
    :return:
    """
    try:
        # print(f'Matriz de tamanho: {len(matriz)}')
        for linha in matriz:
            print("  ".join(linha))
        print("\n")
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
            tamanho = int(input(f"{msg}: "))
            break
        except ValueError:
            print("O valor informado não é um inteiro!")
    return tamanho


def __define_matriz_maior() -> List[List[str]]:
    """
    Metodo de definicao da matriz maior.

    :return:
    """
    # print('MATRIZ MAIOR')
    _tamanho = __define_tamanho(
        msg="Defina a ordem de uma matriz quadrada (de 10 a 20)",
    )
    while _tamanho < 10 or _tamanho > 20:
        print("Valor informado maior que fora do intervalo!")
        _tamanho = __define_tamanho(
            msg="Defina a ordem de uma matriz quadrada (de 10 a 20)",
        )
    matriz = __cria_matriz_quadrada(_tamanho)
    __imprime_matriz(matriz)
    return matriz


def __define_matriz_menor() -> List[List[str]]:
    """
    Cria matriz de padrao.

    :return:
    """
    # print('MATRIZ MENOR')
    matriz = __cria_matriz_quadrada(2)
    __imprime_matriz(matriz)
    return matriz


def __busca_elemento(matriz_maior: list, matriz_menor: list, i: int = 0):
    """
    Metodo recursivo que busca o padrao definido pela matriz menor dentro da matriz maior.

    :param matriz_maior: Matriz principal
    :param matriz_menor: Matriz de padrao
    :param i: Linha da matriz principal
    :return: Lista de resultados
    """
    max_indice = len(matriz_maior) - 1
    if i == max_indice:
        return cordinates
    else:
        for c in range(max_indice):
            matriz_teste = [
                [matriz_maior[i][c], matriz_maior[i][c + 1]],
                [matriz_maior[i + 1][c], matriz_maior[i + 1][c + 1]],
            ]
            if matriz_teste == matriz_menor:
                cordinates.append((i, c))
        return __busca_elemento(matriz_maior, matriz_menor, i + 1)


def __analise_resultado(_resultado, _matriz_menor):
    """
    Escreve os resultados na tela.

    :param _resultado:
    :param _matriz_menor:
    :return:
    """
    print(f"padrao {_matriz_menor}")
    _lista = " ".join([" ".join(linha) for linha in _matriz_menor])
    print(f"lista {_lista}")
    if _resultado:
        print(f"Padrao encontrado nas coordenadas (linha, coluna): {_resultado}")
    else:
        print("Padrao nao encontrado")

    print(f"numero de padrao(oes) encontrado(s): {len(_resultado)}")


def solucao_problema():
    """
    Agrupa os passos do algoritmo.
    :return:
    """
    matriz_maior = __define_matriz_maior()
    matriz_menor = __define_matriz_menor()
    resultado_busca = __busca_elemento(matriz_maior, matriz_menor)
    __analise_resultado(resultado_busca, matriz_menor)


if __name__ == "__main__":
    solucao_problema()

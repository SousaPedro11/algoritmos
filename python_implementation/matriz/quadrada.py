import math

from typing import List, Tuple


def __cria_matriz_quadrada(tamanho: int = 20) -> List[List[str]]:
    matriz = []
    for _ in range(tamanho):
        linha = ["0" for _ in range(tamanho)]
        matriz.append(linha)
    return matriz


def __diagonais(matriz: List[List[str]]) -> Tuple[list, list]:
    tamanho = len(matriz)
    diagonal_principal = []
    diagonal_secundaria = []
    top, bottom, right, left = "B", "A", "Y", "X"

    if tamanho >= 20:
        ponto_medio = math.ceil(tamanho / 2)
        diagonal_principal = [j for j in range(tamanho)]
        diagonal_secundaria = [j for j in range(tamanho)[::-1]]

        for i, j in enumerate(diagonal_secundaria):
            matriz[i][j] = right if (i < ponto_medio) else left
        for i, j in enumerate(diagonal_principal):
            matriz[i][j] = top if (j < ponto_medio) else bottom
    return diagonal_principal, diagonal_secundaria


def __quadrantes(matriz: List[List[str]], diagonal_p: list, diagonal_s: list) -> None:
    tamanho = len(matriz)
    if tamanho >= 20:
        for i in range(tamanho):
            elemento_dp = diagonal_p[i]
            elemento_ds = diagonal_s[i]
            for j in range(tamanho):
                if elemento_dp < j < elemento_ds:
                    matriz[i][j] = "B"
                elif elemento_ds < j < elemento_dp:
                    matriz[i][j] = "A"
                elif j < elemento_dp and j < elemento_ds:
                    matriz[i][j] = "X"
                elif j > elemento_dp and j > elemento_ds:
                    matriz[i][j] = "Y"


def __imprime_matriz(matriz: List[List[str]]) -> None:
    try:
        print(f"Matriz de tamanho: {len(matriz)}")
        for linha in matriz:
            print("  ".join(linha))
        print("\n")
    except ValueError as e:
        print(e)


def __define_tamanho(msg: str) -> int:
    while True:
        try:
            tamanho = int(input(f"{msg}: "))
            break
        except ValueError:
            print("O valor informado não é um inteiro!")
    return tamanho


def __define_matriz_maior() -> List[List[str]]:
    print("MATRIZ MAIOR")
    tamanho = __define_tamanho(
        msg="Defina a ordem de uma matriz quadrada (inteiro maior ou igual a 20)",
    )
    while tamanho < 20:
        print("Valor informado menor que 20!")
        tamanho = __define_tamanho(
            msg="Defina a ordem de uma matriz quadrada (inteiro maior ou igual a 20)",
        )
    matriz = __cria_matriz_quadrada(tamanho)
    diagonal_principal, diagonal_secundaria = __diagonais(matriz)
    __quadrantes(matriz, diagonal_principal, diagonal_secundaria)
    __imprime_matriz(matriz)
    return matriz


def __define_matriz_menor(len_matriz_maior: int) -> List[List[str]]:
    print("MATRIZ MENOR")
    tamanho = __define_tamanho(
        msg=f"Defina a ordem de uma matriz quadrada (inteiro menor que {len_matriz_maior})",
    )
    while tamanho >= len_matriz_maior:
        print(f"Valor informado maior que {len_matriz_maior}!")
        tamanho = __define_tamanho(
            msg=f"Defina a ordem de uma matriz quadrada (inteiro menor que {len_matriz_maior})",
        )
    matriz = __cria_matriz_quadrada(tamanho)
    __imprime_matriz(matriz)
    return matriz


def __gera_matriz_concentrica(
    matriz_maior: List[List[str]], matriz_menor: List[List[str]]
) -> None:
    if len(matriz_menor) > len(matriz_maior):
        raise ValueError("Matriz menor declarada no local errado!")
    print("MATRIZ CONCENTRICA")
    maior = matriz_maior.copy()
    menor = matriz_menor.copy()
    ponto_medio_maior = math.ceil(len(maior) / 2)
    ponto_medio_menor = math.ceil(len(menor) / 2)
    diferenca = ponto_medio_maior - ponto_medio_menor
    for i, linha in enumerate(menor):
        for j, coluna in enumerate(linha):
            maior[i + diferenca][j + diferenca] = coluna
    __imprime_matriz(maior)


def solucao_problema():
    matriz_maior = __define_matriz_maior()
    matriz_menor = __define_matriz_menor(len(matriz_maior))
    __gera_matriz_concentrica(matriz_maior, matriz_menor)


if __name__ == "__main__":
    solucao_problema()

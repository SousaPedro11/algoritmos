import math
from functools import reduce


def fatorial(_number: int) -> int:
    """
    Metodo que calcula o fatorial usando reduce e lambda.

    :param _number: Numero base a ser calculado o fatorial.
    :return: Fatorial de _number
    """
    return 1 if _number in (0, 1) else reduce(lambda x, y: x * y, range(1, _number + 1))


def serie_seno(_angulo: float, n: int):
    """
    Calcula o seno por serie de Taylor.

    :param _angulo: Angulo em radianos
    :param n: Numero de termos da serie
    :return: Seno calculado pela serie
    """
    multiplicador = -1 if n % 2 == 0 else 1
    expoente = 2 * n - 1
    valor = _angulo**expoente
    valor = multiplicador * valor / fatorial(expoente)

    if n == 1:
        return valor
    else:
        return valor + serie_seno(_angulo, n - 1)


def calcula_seno(_angulo: int, n: int) -> float:
    """
    Metodo que chama o calculo pela serie.

    :param _angulo: Angulo para o calculo
    :param n: Numero de termos da serie
    :return: Seno calculado pela serie
    """
    _angulo = math.radians(_angulo)
    return serie_seno(_angulo, n)


def math_seno(_angulo: float) -> float:
    """
    Metodo que utiliza do modulo math para calcular o seno.

    Converte graus em radianos e calcula pela funcao math.sin(x).

    :param _angulo: Angulo de entrada
    :return: Seno calculado pela funcao math.sin()
    """
    return math.sin(math.radians(_angulo))


def compara_calculo_seno(_angulo: int, termos: int = 10):
    """
    Metodo de comparacao entre os dois metodos.

    :param _angulo: Angulo de entrada em graus
    :param termos: Numero de termos da serie, opcional (padrao = 10).
    :return: None
    """
    m_seno = math_seno(_angulo)
    s_seno = calcula_seno(_angulo, termos)
    print(f"Funcao math.sin({_angulo}) = {m_seno}")
    print(f"Serie para o angulo {_angulo} com {termos} termos = {s_seno}")
    print(f"Diferenca entre math.sin e serie = {m_seno - s_seno}")


if __name__ == "__main__":
    angulo = 45
    compara_calculo_seno(angulo)

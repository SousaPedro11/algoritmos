import collections
from unittest import TestCase


def gen_primes(limit):
    """
    Gera a sequencia de numeros primos de 2 ate limit usando o crivo de Eratostenes
    :param limit: valor maximo da amostra
    :return: generator de numeros primos
    """
    # mapa de inteiros compostos para testar sua composicao
    test_map = {}
    # primeiro inteiro de teste
    test_int = 2

    while test_int <= limit:
        if test_int not in test_map:
            # nao marcado  como composto, deve ser primo
            yield test_int
            # primeiro multiplo de test_int ainda nao marcado
            test_map[test_int * test_int] = [test_int]
        else:
            # move cada um para seu proximo multiplo
            for p in test_map[test_int]:
                test_map.setdefault(p + test_int, []).append(p)
            # nao precisa mais do valor, libera a memoria
            del test_map[test_int]
        # incrementa inteiro de teste
        test_int += 1


def gen_groups(primes: list):
    len_grupo = round(len(primes) / 4)
    intervals = [(index * len_grupo, (index + 1) * len_grupo) for index in range(4)]
    keys = ['[00%; 25%]', ']25%; 50%]', ']50%; 75%]', ']75%; 100%]']
    dict_groups = {keys[index]: primes[slice(*intervals[index])] for index in range(4)}
    return dict_groups


def calculate_group_percent(group: list):
    percent_dict = {}
    keys = [1, 3, 5, 7, 9]
    [percent_dict.setdefault(f'{element % 10}', []).append(element) for element in group if element % 10 in keys]
    if '5' not in percent_dict.keys():
        percent_dict['5'] = []
    min_ocorrence, max_ocorrence = percent_dict[str(min(keys))], percent_dict[str(max(keys))]
    percent_dict = collections.OrderedDict(sorted(percent_dict.items()))
    percent_dict = {key: len(value) * 100 / len(group) for key, value in percent_dict.items()}
    percent_dict['max'], percent_dict['min'] = max_ocorrence.__len__(), min_ocorrence.__len__()
    return percent_dict


def data_to_str(data: dict):
    for key, value in data.items():
        str_value = ', '.join(f'{x:02d}' if not isinstance(x, float) else f'{x:0.5f}' for x in value.values())
        data[key] = str_value


def write_file(data: dict):
    headers = ['Intervalo, GPO1, GPO3, GPO5, GPO7, GPO9, Maior, Menor']
    data_to_str(data)
    str_data = headers
    str_data.extend([', '.join(x) for x in zip(data.keys(), data.values())])
    with open('resultados.txt', 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(str_data))


def calculate_avg(dict_percent: dict):
    media = {}


class TestPrime(TestCase):
    """
    Classe base de teste
    """

    def test_primes(self):
        p = gen_primes(1000)
        primes = [i for i in p]
        prime_groups = gen_groups(primes)
        dict_percent = {key: calculate_group_percent(values) for key, values in prime_groups.items()}
        calculate_avg(dict_percent)
        write_file(dict_percent)

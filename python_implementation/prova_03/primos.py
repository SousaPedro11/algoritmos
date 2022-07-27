import collections


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
    """
    Gera o dicionario de grupos
    :param primes: Lista de numeros primos
    :return: Grupos
    """
    # calcula tamanho do fatiamento por grupo
    len_grupo = round(len(primes) / 4)
    # monta a lista de intervalos dos grupos
    intervals = [(index * len_grupo, (index + 1) * len_grupo) for index in range(4)]
    # especifica as chaves dos grupos
    keys = ["[00%; 25%]", "]25%; 50%]", "]50%; 75%]", "]75%; 100%]"]
    # monta os grupos a partir da lista de intervalos associando as chaves aos respectivos intervalos
    dict_groups = {keys[index]: primes[slice(*intervals[index])] for index in range(4)}
    return dict_groups


def calculate_group_percent(group: list):
    """
    Gera dicionario com percentual de ocorrencias dos numero definidos
    :param group: Grupos
    :return: Dicionario com percentual de ocorrencias
    """
    # inicializa o dicionario
    percent_dict = {}
    # define a lista de chaves
    keys = [1, 3, 5, 7, 9]
    # calcula o ultimo digito de cada elemento dos grupos e adiciona a respectiva chave existente
    [
        percent_dict.setdefault(f"{element % 10}", []).append(element)
        for element in group
        if element % 10 in keys
    ]
    # caso em algum grupo nao exista a chave 5, adiciona a chave com o valor sendo uma lista vazia
    if "5" not in percent_dict.keys():
        percent_dict["5"] = []
    # caso min e max sejam numeros de ocorrencias, descomente aqui
    # min_ocorrence, max_ocorrence = percent_dict[str(min(keys))], percent_dict[str(max(keys))]

    # ordena o dicionario pelas chaves
    percent_dict = collections.OrderedDict(sorted(percent_dict.items()))
    # calcula a porcentagem de ocorrencias para cada chave e substitui a lista de elementos pelo valor calculado
    percent_dict = {
        key: len(value) * 100 / len(group) for key, value in percent_dict.items()
    }

    # caso min e max sejam numeros de ocorrencias, descomente aqui
    # percent_dict['max'], percent_dict['min'] = max_ocorrence.__len__(), min_ocorrence.__len__()

    # caso min e max sejam numeros de ocorrencias, comente as 2 linhas abaixo
    min_ocorrence, max_ocorrence = (
        percent_dict[str(min(keys))],
        percent_dict[str(max(keys))],
    )
    percent_dict["max"], percent_dict["min"] = max_ocorrence, min_ocorrence
    return percent_dict


def add_avg_in_dict(dict_percent: dict):
    """
    Adiciona a media de ocorrencias de cada numero ao dicionario
    :param dict_percent: Dicionario de percentual dos grupos
    :return: None
    """
    # inicializa a lista de valores do dicionario, corresponde aos dicionarios que representam o conjunto de ocorrencias
    valores = list(dict_percent.values())
    # calcula a media de cada chave a partir dos valores de todos os grupos
    media_values = {
        key: sum(d[key] for d in valores) / len(valores) for key in valores[0].keys()
    }
    # adiciona chave-valor correspondente a media ao dicionario
    dict_percent["Média"] = media_values


def data_to_str(data: dict):
    """
    Prepara o dicionario para a saida convertendo os valores para string concatenada
    :param data: Dicionario de percentual dos grupos
    :return: Dados formatados
    """
    _data = {}
    # percorre chave, valor dos elementos do dicionario de grupos
    for key, value in data.items():
        # concatena os valores de cada coluna com ', ' entre eles, formatando com base no tipo numerico
        str_value = ", ".join(
            f"{x:02d}" if not isinstance(x, float) else f"{x:0.5f}"
            for x in value.values()
        )
        # substitui os valores de cada grupo pelo seu correspondente transformado em string
        _data[key] = str_value
    return _data


def prepare_data_to_output(data):
    """
    Formata os dados para escrita
    :param data: Dicionario com os dados dos grupos
    :return: Dados formatados
    """
    # adiciona o cabecalho da saida
    headers = ["Intervalo, GPO1, GPO3, GPO5, GPO7, GPO9, Maior, Menor"]
    # transforma os dados em string
    _data = data_to_str(data)
    # inicializa os dados de saida com o valor de header
    str_data = headers
    # adiciona cada grupo em formato de string concatenada de chave-valor aos dados de saida
    str_data.extend([", ".join(x) for x in zip(_data.keys(), _data.values())])
    # retorna os dados de saida
    return str_data


def write_file(data: dict):
    """
    Escreve os dados formatados em arquivo
    :param data: Dados formatados
    :return: None
    """
    # transforma os dados em string para a saida
    str_data = prepare_data_to_output(data)
    # nome do arquivo de saida
    file_name = "resultados.txt"
    # container que abre/fecha o arquivo em modo de escrita
    with open(file_name, "w", encoding="utf-8") as f:
        # escreve as linhas a partir da lista de dados adicionando um enter no final
        f.writelines("\n".join(str_data))


def write_prompt(data: dict):
    """
    Imprime os dados na tela
    :param data: Dados a serem impressos
    :return: None
    """
    # transforma os dados em string para a saida
    str_data = prepare_data_to_output(data)
    # percorre a lista de dados imprimindo-os na tela
    for value in str_data:
        print(value)


def solucao():
    """
    Metodo que segue o passo a passo para solucionar a questao
    :return: None
    """
    primes = list(gen_primes(1000))
    prime_groups = gen_groups(primes)
    dict_percent = {
        key: calculate_group_percent(values) for key, values in prime_groups.items()
    }
    add_avg_in_dict(dict_percent)
    # comentar caso nao precise gerar o arquivo
    write_file(dict_percent)
    write_prompt(dict_percent)


if __name__ == "__main__":
    solucao()

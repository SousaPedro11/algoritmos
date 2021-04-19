def divisao(num1: int, num2: int) -> float:
    return num1/num2


a = int(input('Informe o dividendo: '))
b = int(input('Informe o divisor: '))

c = divisao(a, b)

print('\nRESULTADO')
print(f'Sem formatação:\n{a}/{b} = {c}\n')
print(f'Com formatação:\n{a}/{b} = {c:.2f}')

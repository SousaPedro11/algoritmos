"""
Autor: Pedro Sousa
Data: 17/03/2021
Numero da questao: Questão 10
Descriçao do problema:
    mplemente uma classe chamada Carro que atenda aos requisitos abaixo.
    a. Um veículo tem um certo consumo de combustível (medidos em km / litro)
    e uma certa quantidade de combustível no tanque.
    b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
    c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma
    certa distância, reduzindo o nível de combustível no tanque de gasolina.
    d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    e. Forneça um método adicionarGasolina( ), para abastecer o tanque.
Descricao da solucao:
    * Criei uma classe para usar testes unitários apenas chamando um método solv()
    com a classe instanciada.
    * Criei um construtor para testar com outros valores de quantidade de pessoas
    O método solv() chama métodos auxiliares e resolve item a item

Versão do Python: 3.9.2
Versão do Pytest: 6.2.2
"""


class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    @property
    def consumo(self):
        return self._consumo

    @consumo.setter
    def consumo(self, consumo: float):
        self._consumo = consumo

    @property
    def combustivel(self):
        return self._combustivel

    @combustivel.setter
    def combustivel(self, combustivel: float):
        self._combustivel = combustivel

    def adicionar_gasolina(self, gasolina: float):
        print(f"Adicionando {gasolina} l de gasolina")
        self._combustivel += gasolina

    def andar(self, distancia):
        consumido = distancia / self.consumo
        if consumido > self.combustivel:
            percorrido = self.consumo * self.combustivel
            raise Exception(
                f"É possível percorrer apenas {percorrido} Km com a quantidade de combustível atual"
            )
        print(f"Carro andou {distancia} Km")
        print(f"Carro consumiu {consumido:.2f} l")
        self.combustivel -= consumido

    def obter_gasolina(self):
        print(f"Gasolina atual: {self.combustivel:.2f} l")


class Consumo:
    def solv(self):
        """
        Método que soluciona o problema
        """
        try:
            carro = Carro(15)
            carro.obter_gasolina()
            print(f"Carro faz {carro.consumo} Km/l")
            carro.adicionar_gasolina(20)
            carro.andar(100)
            carro.obter_gasolina()
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    Consumo().solv()

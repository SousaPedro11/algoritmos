class Programa:
    """
    Super classe
    """

    def __init__(self, nome: str, ano: int):
        self._nome = nome.title()
        self.ano = ano
        self._likes: int = 0

    @property
    def likes(self) -> int:
        return self._likes

    def dar_like(self) -> None:
        self._likes += 1

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome.title()

    def __str__(self) -> str:
        nome: str = f'\nNome: {self._nome}\n'
        ano: str = f'Ano: {self.ano}\n'
        like: str = f'Likes: {self._likes} Likes\n'
        return nome + ano + like


class Filme(Programa):
    """
    Classe filha
    """

    def __init__(self, nome: str, ano: int, duracao: int):
        # com esta ação estamos usando nome e ano da classe mãe Programa
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self) -> str:
        duracao: str = f'Duração: {self.duracao} min\n'
        return super(Filme, self).__str__() + duracao


programa = Programa('TV Cruj', 1998)
programa.dar_like()
print(programa)

filme = Filme('Careca de trança', 2000, 120)
(lambda x: filme.dar_like(), range(10))()
print(filme)

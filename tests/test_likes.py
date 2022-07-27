from python_implementation.likes import Filme, Programa


# programa = Programa("TV Cruj", 1998)
# programa.dar_like()
# print(programa)

# filme = Filme("Careca de trança", 2000, 120)

# for _ in range(10):
#     filme.dar_like()

# print(filme)


class TestFilme:
    def test_programa(self):
        programa = Programa("TV Cruj", 1998)
        programa.dar_like()
        assert programa.likes == 1
        assert programa.nome == "TV Cruj".title()
        assert programa.ano == 1998

    def test_filme(self):
        filme = Filme("Careca de trança", 2000, 120)
        for _ in range(10):
            filme.dar_like()
        assert filme.likes == 10
        assert filme.nome == "Careca de trança".title()
        assert filme.ano == 2000
        assert filme.duracao == 120

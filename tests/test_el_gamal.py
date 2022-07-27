import random
from python_implementation.el_gamal import ElGamal


class TestElGamal:
    def test_el_gamal(self, monkeypatch):
        el_gamal = ElGamal()
        message_input = "Há vagas nessa joça"

        big_number = random.randint(pow(11, 20) + 1, pow(11, 50) + 1)

        random_element = random.randint(2, big_number)

        private_key = el_gamal.gerar_chave(big_number)

        modular_exponent = el_gamal.expoente_modular(
            random_element, private_key, big_number
        )

        criptography_message, public_key = el_gamal.criptografar_mensagem(
            message_input, big_number, modular_exponent, random_element
        )
        decifred_message = el_gamal.decifrar(
            criptography_message, public_key, private_key, big_number
        )

        assert message_input == "".join(decifred_message)

from io import StringIO
from random import randint

import pytest
from python_implementation.divisao import Divisao


class TestDivisao:
    def test_divisao(self, monkeypatch):
        user_input_dividendo = randint(-10, 10)
        user_input_divisor = randint(1, 10)
        monkeypatch.setattr(
            "sys.stdin", StringIO(f"{user_input_dividendo}\n{user_input_divisor}\n")
        )
        output = Divisao().solv()
        assert output == user_input_dividendo / user_input_divisor

    def test_divisao_with_zero_divisor(self, monkeypatch):
        user_input_dividendo = randint(-10, 10)
        user_input_divisor = 0

        with pytest.raises(
            ZeroDivisionError,
            match=r"^division by zero$",
        ):
            monkeypatch.setattr(
                "sys.stdin", StringIO(f"{user_input_dividendo}\n{user_input_divisor}\n")
            )
            output = Divisao().solv()
            assert output == user_input_dividendo / user_input_divisor

from io import StringIO
from random import randint

import pytest

from python_implementation.cap_seis import CapSeisUm


class TestCap6:
    def test_cap_seis_um(self, monkeypatch):
        user_input = randint(-10, 10)
        monkeypatch.setattr("sys.stdin", StringIO(f"{user_input}\n"))
        output = CapSeisUm().solv()
        assert output == user_input - 1

    def test_cap_seis_um_dois(self, monkeypatch):
        user_input = randint(-10, 10) / 1.0

        with pytest.raises(
            ValueError,
            match=r"^invalid literal for int\(\) with base 10: '.*'$",
        ):
            monkeypatch.setattr("sys.stdin", StringIO(f"{user_input}\n"))
            output = CapSeisUm().solv()
            assert output == user_input - 1.0

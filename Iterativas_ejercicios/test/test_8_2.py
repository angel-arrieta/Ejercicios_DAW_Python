import pytest
from src.Ej_8_2 import escalera


@pytest.mark.parametrize(
    "inNiveles, outMensaje",
    [
        (3, " 1\n 3 1\n 5 3 1"),
        (4, " 1\n 3 1\n 5 3 1\n 7 5 3 1"),
        (5, " 1\n 3 1\n 5 3 1\n 7 5 3 1\n 9 7 5 3 1")
    ]
)


def test_escalera(inNiveles, outMensaje):
    assert escalera(inNiveles) == outMensaje
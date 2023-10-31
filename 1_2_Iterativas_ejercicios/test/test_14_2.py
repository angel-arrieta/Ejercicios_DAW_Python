import pytest
from src.Ej_14_2 import sumar


@pytest.mark.parametrize(
    "inTotal, inActual, outMensaje",
    [
        (0, 5, 5),
        (15, 4, 19),
        (19, -3, 16),
        (16, 0, "fuera")
    ]
)


def test_sumar(inTotal, inActual, outMensaje):
    assert sumar(inTotal, inActual) == outMensaje
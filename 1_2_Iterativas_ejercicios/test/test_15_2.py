import pytest
from src.Ej_15_2 import sumar_positivos


@pytest.mark.parametrize(
    "inTotal, inActual, outMensaje",
    [
        (0, 5, 5),
        (7, -4, 7),
        (7, 3, 10),
        (16, 0, "fuera")
    ]
)


def test_sumar_positivos(inTotal, inActual, outMensaje):
    assert sumar_positivos(inTotal, inActual) == outMensaje
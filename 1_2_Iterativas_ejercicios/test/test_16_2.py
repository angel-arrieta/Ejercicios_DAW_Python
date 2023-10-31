import pytest
from src.Ej_16_2 import comparador


@pytest.mark.parametrize(
    "inAnterior, inActual, outMensaje",
    [
        (0, 5, 5),
        (5, 3, 5),
        (5, 21, 21),
        (21, 0, "fuera")
    ]
)


def test_comparador(inAnterior, inActual, outMensaje):
    assert comparador(inAnterior, inActual) == outMensaje
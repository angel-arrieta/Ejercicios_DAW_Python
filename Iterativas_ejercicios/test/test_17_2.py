import pytest
from src.Ej_17_2 import suma_digitos


@pytest.mark.parametrize(
    "inNumero, outMensaje",
    [
        (15, 6),
        (324, 9),
        (10, 1),
        (5, 5)
    ]
)


def test_suma_digitos(inNumero, outMensaje):
    assert suma_digitos(inNumero) == outMensaje
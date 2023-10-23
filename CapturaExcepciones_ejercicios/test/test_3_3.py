import pytest
from src.Ej_3_3 import cuentaAtras


@pytest.mark.parametrize(
    "inEjemplo, outMensaje",
    [
        (1, "1, 0"),
        (3, "3, 2, 1, 0"),
        (7, "7, 6, 5, 4, 3, 2, 1, 0"),
    ]
)


def test_cuentaAtras(inEjemplo, outMensaje):
    assert cuentaAtras(inEjemplo) == outMensaje

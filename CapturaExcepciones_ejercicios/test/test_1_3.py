import pytest
from src.Ej_1_3 import unaVida


@pytest.mark.parametrize(
    "inEdad, outMensaje",
    [
        (9, "1\n2\n3\n4\n5\n6\n7\n8\n9"),
        (5, "1\n2\n3\n4\n5"),
        (0, "0")
    ]
)


def test_unaVida(inEdad, outMensaje):
    assert unaVida(inEdad) == outMensaje

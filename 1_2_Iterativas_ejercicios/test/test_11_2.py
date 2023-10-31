import pytest
from src.Ej_11_2 import recorre_inversa


@pytest.mark.parametrize(
    "inPalabra, outMensaje",
    [
        ("pendejo", "o\nj\ne\nd\nn\ne\np"),
        ("amigo", "o\ng\ni\nm\na"),
        ("ordenador", "r\no\nd\na\nn\ne\nd\nr\no")
    ]
)


def test_recorre_inversa(inPalabra, outMensaje):
    assert recorre_inversa(inPalabra) == outMensaje

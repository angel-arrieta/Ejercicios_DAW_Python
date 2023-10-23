import pytest
from src.Ej_6_2 import triangulo


@pytest.mark.parametrize(
    "inNiveles, outMensaje",
    [
        (1, "*"),
        (2, "*\n**"),
        (3, "*\n**\n***"),
        (4, "*\n**\n***\n****"),
        (5, "*\n**\n***\n****\n*****")
    ]
)


def test_triangulo(inNiveles, outMensaje):
    assert triangulo(inNiveles) == outMensaje
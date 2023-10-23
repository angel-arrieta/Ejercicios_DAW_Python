import pytest
from src.Ej_21_2 import compra, descuento


@pytest.mark.parametrize(
    "inTotal, inNuevo, outTotal",
    [
        (0, 45, 45),
        (45, -7, 45),
        (45, 0, 45)
    ]
)


def test_compra(inTotal, inNuevo, outTotal):
    assert compra(inTotal, inNuevo) == outTotal


@pytest.mark.parametrize(
    "inTotal, outTotal",
    [
        (500, 500),
        (1000, 900),
        (1453, 1307.7)
    ]
)


def test_descuento(inTotal, outTotal):
    assert descuento(inTotal) == outTotal
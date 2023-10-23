import pytest
from src.Ej_24_2 import contador_primos


@pytest.mark.parametrize(
    "inLista, outEncontrados",
    [
        ([2, 6, 4, 5, 10, 7, 8, 3, 7], 5),
        ([7, 4, 9, 24, 23, 16, 7, 11], 4)
    ]
)


def test_contador_primos(inLista, outEncontrados):
    assert contador_primos(inLista) == outEncontrados

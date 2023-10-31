import pytest
from src.AlgBurb_conInput import algoritmo_burbuja


@pytest.mark.parametrize(
    "inLista, outLista",
    [
        ([10, 2, 8], [2, 8, 10]),
        ([15, 5, 8, 14, 21], [5, 8, 14, 15, 21]),
        ([43, 27, 3, 32, 15, 7, 21], [3, 7, 15, 21, 27, 32, 43])
    ]
)


def test_algoritmo_burbuja(inLista, outLista):
    assert algoritmo_burbuja(inLista) == outLista

import pytest
from src.Ej_2_3 import impares


@pytest.mark.parametrize(
    "inRango, outMensaje",
    [
        (2, "1"),
        (3, "1, 3"),
        (8, "1, 3, 5, 7"),
    ]
)


def test_impares(inRango, outMensaje):
    assert impares(inRango) == outMensaje

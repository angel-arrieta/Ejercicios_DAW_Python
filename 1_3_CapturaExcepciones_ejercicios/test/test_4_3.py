import pytest
from src.Ej_4_3 import esEntero


@pytest.mark.parametrize(
    "inNumero, outBoolean",
    [
        (1, False),
        ("tre", True),
        ([0, "aju"], True)
    ]
)


def test_esEntero(inNumero, outBoolean):
    assert esEntero(inNumero) == outBoolean

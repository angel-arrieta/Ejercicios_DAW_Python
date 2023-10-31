import pytest
from src.Ej_4_0 import cuenta, control_letra


@pytest.mark.parametrize(
    "inPalabra, inLetra, outVeces",
    [
        ("Entrada", "A", 2),
        ("ESTACIONAMIENTO", "i", 2)
    ]
)
def test_cuenta(inPalabra, inLetra, outVeces):
    assert cuenta(inPalabra, inLetra) == outVeces


@pytest.mark.parametrize(
    "inLetra, outFallo",
    [
        ("", 1),
        ("8i", 2),
        ("!", 3),
        ("R", 0),
    ]
)
def test_control_letra(inLetra, outFallo):
    assert control_letra(inLetra) == outFallo

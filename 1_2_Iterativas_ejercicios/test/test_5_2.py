import pytest
from src.Ej_5_2 import inversion


@pytest.mark.parametrize(
    "inMonto_inicial, inInteres, inAnos, outMensaje",
    [
        (100, 15, 1, "Año 1 -- 115.0"),
        (200, 5, 3, "Año 1 -- 210.0\nAño 2 -- 220.5\nAño 3 -- 231.53")
    ]
)

def test_inversion(inMonto_inicial, inInteres, inAnos, outMensaje):
    assert inversion(inMonto_inicial, inInteres, inAnos) == outMensaje

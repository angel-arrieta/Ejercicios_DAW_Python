import pytest
from src.Ej_0_3 import function


@pytest.mark.parametrize(
    "inMensaje, outMensaje",
    [
        ("Entrada1", "Salida1"),
        ("Entrada2", "Salida2")
    ]
)
def test_function(inMensaje, outMensaje):
    assert function(inMensaje) == outMensaje

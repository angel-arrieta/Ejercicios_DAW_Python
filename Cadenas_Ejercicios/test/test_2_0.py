import pytest
from src.Ej_2_0 import explicacion_ejercicio


@pytest.mark.parametrize(
    "inPalabra, outExplicacion",
    [
        ("patata", (f"Teniendo la palabra patata, sabemos que es una cadena. "
    f"El significado de 'patata[:]' es lo mismo,\n"
    f"lo obviamente diferente '[:]' es para aplicar la operación"
    f"'slicing' (rebanado), por la cual se extraen\n"
    f"elementos a la cadena u otras secuencias")),
        ("Rata", (f"Teniendo la palabra Rata, sabemos que es una cadena. "
    f"El significado de 'Rata[:]' es lo mismo,\n"
    f"lo obviamente diferente '[:]' es para aplicar la operación"
    f"'slicing' (rebanado), por la cual se extraen\n"
    f"elementos a la cadena u otras secuencias"))
    ]
)
def test_explicacion_ejercicio(inPalabra, outExplicacion):
    assert explicacion_ejercicio(inPalabra) == outExplicacion

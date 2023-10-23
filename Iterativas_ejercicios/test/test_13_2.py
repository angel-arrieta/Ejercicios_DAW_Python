import pytest
from src.Ej_13_2 import resonar


@pytest.mark.parametrize(
    "inGrito, outMensaje",
    [
        ("Hola", "Hola"),
        ("Saludos", "Saludos"),
        ("Okay, let's go", "Okay, let's go"),

    ]
)


def test_resonar(inGrito, outMensaje):
    assert resonar(inGrito) == outMensaje
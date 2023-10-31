import pytest
from src.Ej_20_2 import buscador_caracteres


@pytest.mark.parametrize(
    "inFrase, inLetra, outMensaje",
    [
        ("Un video mas para perder el tiempo", "i", "Posiciones donde no esta 1, 2, 3, 4. Encontrado en posición 5."),
        ("Saracatunga", "a", "Posiciones donde no esta 1. Encontrado en posición 2."),
        ("Borrego estupido", "s", "Posiciones donde no esta 1, 2, 3, 4, 5, 6, 7, 8, 9. Encontrado en posición 10.")

    ]
)


def test_buscador_caracteres(inFrase, inLetra, outMensaje):
    assert buscador_caracteres(inFrase, inLetra) == outMensaje
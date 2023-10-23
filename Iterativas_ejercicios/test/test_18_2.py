import pytest
from src.Ej_18_2 import contador_paridad, suma_digitos


@pytest.mark.parametrize(
    "inPares, inImpares, inNuevo, outPar_Impar",
    [
        (0, 0, 7, (0, 1)),
        (0, 1, 8, (1, 1)),
        (5, 3, 17, (5, 4))
    ]
)


def test_contador_paridad(inPares, inImpares, inNuevo, outPar_Impar):
    assert contador_paridad(inPares, inImpares, inNuevo) == outPar_Impar


@pytest.mark.parametrize(
    "inNumero, outSuma",
    [
        (0, 0),
        (-1, 1),
        (15, 6),
        (37, 10),
        (184, 13),
        (-47, 11)
    ]
)


def test_suma_digitos(inNumero, outSuma):
    assert suma_digitos(inNumero) == outSuma
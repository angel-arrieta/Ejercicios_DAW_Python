import pytest
from src.Ej_22_2 import paridad_digitos


@pytest.mark.parametrize(
    "inNumero, outPar, outImpar",
    [
        (457, 1, 2),
        (13822, 3, 2)
    ]
)


def test_paridad_digitos(inNumero, outPar, outImpar):
    assert paridad_digitos(inNumero) == (outPar, outImpar)

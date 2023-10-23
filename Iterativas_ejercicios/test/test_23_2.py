import pytest
from src.Ej_23_2 import cuenta_digitos, cuenta_lineas


@pytest.mark.parametrize(
    "inLinea, outDigitos",
    [
        (["Los 3 mosqueteros", "Historia de 2 ciudades"], 2)
    ]
)


def test_cuenta_digitos(inLinea, outDigitos):
    assert cuenta_digitos(inLinea) == outDigitos


@pytest.mark.parametrize(
    "inRegistro, outNumeroLineas",
    [
        ([["Los 3 mosqueteros", "Historia de 2 ciudades"], ["101 Dalmatas", "100 años de soledad"]], 2 )
    ]
)


def test_cuenta_lineas(inRegistro, outNumeroLineas):
    assert cuenta_lineas(inRegistro) == outNumeroLineas

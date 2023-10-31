import pytest
from src.Ej_7_2 import tablaMultiplicar


@pytest.mark.parametrize(
    "inNumero, outMensaje",
    [
        (4, "1 * 4 = 4\n2 * 4 = 8\n3 * 4 = 12\n4 * 4 = 16\n5 * 4 = 20\n6 * 4 = 24\n7 * 4 = 28\n8 * 4 = 32\n9 * 4 = 36\n10 * 4 = 40"),
        (6, "1 * 6 = 6\n2 * 6 = 12\n3 * 6 = 18\n4 * 6 = 24\n5 * 6 = 30\n6 * 6 = 36\n7 * 6 = 42\n8 * 6 = 48\n9 * 6 = 54\n10 * 6 = 60")
    ]
)


def test_tablaMultiplicar(inNumero, outMensaje):
    assert tablaMultiplicar(inNumero) == outMensaje
from src.Ej_4_2 import cuentaAtras


def test_cuentaAtras():
    assert cuentaAtras(10) == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"

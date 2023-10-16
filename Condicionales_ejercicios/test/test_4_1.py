from src.Ej_4_1 import paridad


def test_paridad():
    assert paridad(5) == "Tu número es impar"
    assert paridad(8) == "Tu número es par"

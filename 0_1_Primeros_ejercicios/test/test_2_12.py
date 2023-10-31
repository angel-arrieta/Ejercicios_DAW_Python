from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_12 import calculadora_imc


def test_calculadora_imc():
    assert calculadora_imc(90, 1.60) == f"Tú índice de masa corporal es {90 / 1.60**2}"

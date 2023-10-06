from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_11 import sumatorio


def test_sumatorio():
    assert sumatorio(9) == f"El sumatorio de {9} es {9 * (9 +1) / 2}"

from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_6 import sustraer_iva


def test_sustraer_iva():
    assert sustraer_iva(75) == f"El precio inicial es {75 / 110 * 100}"

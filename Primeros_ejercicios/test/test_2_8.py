from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_8 import suman , sumar


def test_suman():
    assert suman(1, 2,) == 1 + 2

def test_sumar():
    assert sumar(3, 4) == f"El resultado da {3 + 4}"
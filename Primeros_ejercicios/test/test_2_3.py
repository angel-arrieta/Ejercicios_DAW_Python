from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_3 import cuentas


def test_cuentas():
    assert cuentas(17, 12.0) == ("""1. 8.5
    2. 8
    3. 4.0
    4. 11 """)

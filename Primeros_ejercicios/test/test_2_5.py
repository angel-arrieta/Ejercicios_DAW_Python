from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_5 import calcular_iva


def test_calcular_iva():
    assert calcular_iva(50, 21) == f"El precio con IVA es {50 + 50 / 100 * 21}"

from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_14 import peso_paquete


def test_peso_paquete():
    assert peso_paquete(5, 7) == f"El paquete pesa {(5 * 112 + 7 * 75) / 100} kilogramos"

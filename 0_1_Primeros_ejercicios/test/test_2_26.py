from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_26 import lista_compra


def test_lista_compra():
    assert lista_compra("cuaderno, mochila, folios") == f"cuaderno\n mochila\n folios"

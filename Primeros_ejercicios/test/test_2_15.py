from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_15 import intereses


def test_intereses():
    assert intereses(100) == (f"El primer año acabas con 104.0 euros\n"
    f"El segundo año acabas con 108.16 euros\n"
    f"El tercer año acabas con 112.49 euros")

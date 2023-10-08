from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_16 import barras_pasadas


def test_barras_pasadas():
    assert barras_pasadas(50) == (f"Cada barra se vende a 3.49 euros, sí no es fresca se le descuenta un 60½\n"
    f"Se ha conseguido 104.7 euros de barras que no son del día")

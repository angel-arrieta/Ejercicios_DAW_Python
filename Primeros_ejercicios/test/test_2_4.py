from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_4 import conv_a_Fahrenheit


def test_conv_a_Fahrenheit():
    assert conv_a_Fahrenheit(17) == f"{17}ºC son {17 * 1.8 + 32}ºF"
from Ejercicios_DAW_Python.Primeros_ejercicios.src.Ej_2_27 import calculadora_producto


def test_calculadora_producto():
    assert calculadora_producto("tomate", 1.5, 4) == (f"tomate vale 000001.50\n"
    f"004 tomate vale 00000006.00")

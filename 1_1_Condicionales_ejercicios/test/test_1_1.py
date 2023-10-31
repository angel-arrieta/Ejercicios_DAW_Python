from src.Ej_1_1 import Comprobacion_edad


def test_Comprobacion_edad():
    assert Comprobacion_edad(15) == "Es menor de edad"
    assert Comprobacion_edad(19) == "Es mayor de edad"
    assert Comprobacion_edad(-1) == "Error al introducir la edad"

from src.Ej_2_1 import Comprueba_contrasena


def test_Comprueba_contrasena():
    assert Comprueba_contrasena("Hola") == "Contraseña equivocada"
    assert Comprueba_contrasena("contraseña") == "Contraseña correcta"

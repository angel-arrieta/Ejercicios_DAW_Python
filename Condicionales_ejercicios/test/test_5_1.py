from src.Ej_5_1 import comprobar_tributar


def test_comprobar_tributar():
    assert comprobar_tributar(14, 900) == "Usted no debe tributar"
    assert comprobar_tributar(15, 1200) == "Usted no debe tributar"
    assert comprobar_tributar(17, 1500) == "Usted debe tributar"
    assert comprobar_tributar(21, 850) == "Usted no debe tributar"

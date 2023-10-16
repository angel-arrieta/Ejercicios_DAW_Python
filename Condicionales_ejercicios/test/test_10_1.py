from src.Ej_10_1 import menu, anadir, comanda


def test_menu():
    assert menu("si") == ["pimiento", "tofu"]
    assert menu("no") == ["pimiento", "tofu", "peperoni", "jamón", "salmón"]
    assert menu("Hola") == "Error"


def test_anadir():
    assert anadir(["tomate", "queso"], "tomate") == (["queso"], "tomate")
    assert anadir(["tomate", "queso"], "sardina") == "no_hay"
    assert anadir(["tomate", "queso"], "salir") == "fuera"


def test_comanda():
    assert comanda(["tomate", "queso", "pimiento", "tofu"], "si") == ("vegetariana ", "tomate, queso, pimiento, tofu")
    assert comanda(["tomate", "queso", "jamón", "pimiento"], "no") == ("", "tomate, queso, jamón, pimiento")

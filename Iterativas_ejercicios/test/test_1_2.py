from src.Ej_1_2 import decamultiplicador


def test_decamultiplicador():
    assert decamultiplicador("Gungiga") == "Gungiga\nGungiga\nGungiga\nGungiga\nGungiga\nGungiga\nGungiga\nGungiga\nGungiga\nGungiga\n"
    assert decamultiplicador("0") == "0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n"
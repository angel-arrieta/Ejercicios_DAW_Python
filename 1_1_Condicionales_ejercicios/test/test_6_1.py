from src.Ej_6_1 import division


def test_division():
    assert division("hombre", "Angel") == "Estas en el grupo B"
    assert division("hombre", "Raul") == "Estas en el grupo A"
    assert division("mujer", "Angela") == "Estas en el grupo A"
    assert division("mujer", "Sara") == "Estas en el grupo B"

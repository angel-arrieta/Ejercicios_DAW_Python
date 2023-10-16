from src.Ej_3_1 import division


def test_division():
    assert division(10,2) == "5.0"
    assert division(8,0) == "Error, la operación es indivisible"

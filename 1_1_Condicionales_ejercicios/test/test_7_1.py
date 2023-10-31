from src.Ej_7_1 import declaracion


def test_declaracion():
    assert declaracion(900) == "Su renta anual es del 5%"
    assert declaracion(15000) == "Su renta anual es del 15%"
    assert declaracion(27500) == "Su renta anual es del 20%"
    assert declaracion(43500) == "Su renta anual es del 30%"
    assert declaracion(71000) == "Su renta anual es del 45%"
    assert declaracion(-5) == "Valor de renta sin sentido"

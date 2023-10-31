from src.Ej_8_1 import evaluacion


def test_evaluacion():
    assert evaluacion(0.0) == "Evaluación inaceptable, sin bonificación obtenida"
    assert evaluacion(0.2) == "Datos Introducidos ilegibles o incorrectos"
    assert evaluacion(0.4) == f"Evaluación aceptable, bonificación de {0.4 * 2400} obtenida"
    assert evaluacion(0.8) == f"Evaluación meritoria obtenida, bonificación de {0.8 * 2400}"
    assert evaluacion(-0.3) == "Datos Introducidos ilegibles o incorrectos"
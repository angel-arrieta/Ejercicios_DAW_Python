from src.Ej_9_1 import entrada


def test_entrada():
    assert entrada(-1) == "Perdona, pero no lo entendi bien"
    assert entrada(3) == "¿A que esperas? ¡Entra adentro, chic@!"
    assert entrada(12) == "¡Por 5 euros puedes entrar, chaval!"
    assert entrada(21) == "Por solo 10 euros puede entrar, jovencit@"
    assert entrada(30) == "Buenas señor/a debe pagar 10 euros por la entrada"

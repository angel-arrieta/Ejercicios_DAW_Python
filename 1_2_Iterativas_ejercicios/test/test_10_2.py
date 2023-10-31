import pytest
from src.Ej_10_2 import primo


@pytest.mark.parametrize(
    "inUsuario, outMensaje",
    [
        (0, "0 no es primo."),
        (1, "1 no es primo."),
        (-1, "-1 no es primo."),
        (5, "5 es primo."),
        (-7, "-7 es primo."),
        (4, "4 no es primo."),
        (-6, "-6 no es primo.")
    ]
)

def test_primo(inUsuario, outMensaje):
    assert primo(inUsuario) == outMensaje
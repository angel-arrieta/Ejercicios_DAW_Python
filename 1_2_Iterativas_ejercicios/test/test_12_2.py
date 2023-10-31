import pytest
from src.Ej_12_2 import recurrencia


@pytest.mark.parametrize(
    "inFrase, inLetra, outMensaje",
    [
        ("Un video mas mi gente", "e", 3),
        ("Salsa y picante", "a", 3)
    ]
)


def test_recurrencia(inFrase, inLetra, outMensaje):
    assert recurrencia(inFrase, inLetra) == outMensaje
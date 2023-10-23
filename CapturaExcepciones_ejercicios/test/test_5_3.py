import pytest
from src.Ej_5_3 import contrasena


@pytest.mark.parametrize(
    "inUsuario, outBoolean",
    [
        ("trebol", False),
        (1, False),
        (["haha", 37], False),
        ("contrasena", True)
    ]
)


def test_contrasena(inUsuario, outBoolean):
    assert contrasena(inUsuario) == outBoolean

import pytest
from src.Ej_9_2 import identificacion


@pytest.mark.parametrize(
    "inUsuario, outMensaje",
    [
        ("trebol", "incorrecta"),
        ("contraseña", "correcta")
    ]
)


def test_identificacion(inUsuario, outMensaje):
    assert identificacion(inUsuario) == outMensaje
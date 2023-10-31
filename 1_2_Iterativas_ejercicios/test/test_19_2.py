import pytest
from src.Ej_19_2 import menu


@pytest.mark.parametrize(
    "inOpcion, outMensaje",
    [
        (1, """COMENZAR Programa-dolor sit amet, consectetur adipiscing elit.
        Maecenas justo mi, accumsan eu lorem at, ultricies rutrum
        massa. Mauris ac magna vel lorem ultrices tincidunt.
        Nullam vel sem orci. Nullam finibus ex orci. Nullam vitae
        odio sodales, ultricies risus at, imperdiet quam."""),
        (2, """ IMPRIMIR Listado-dolor sit amet, consectetur adipiscing elit.
         Maecenas justo mi, accumsan eu lorem at, ultricies rutrum
         massa. Mauris ac magna vel lorem ultrices tincidunt.
         Nullam vel sem orci. Nullam finibus ex orci. Nullam vitae
         odio sodales, ultricies risus at, imperdiet quam."""),
        (3, "Saliendo"),
        (0, "Opción incorrecta, vuelva a intentar"),
        (4, "Opción incorrecta, vuelva a intentar")
    ]
)


def test_menu(inOpcion, outMensaje):
    assert menu(inOpcion) == outMensaje
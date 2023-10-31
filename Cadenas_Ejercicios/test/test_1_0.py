import pytest
from src.Ej_1_0 import revertir_cadena


@pytest.mark.parametrize(
    "inCadena_inicial, outReversa_newline",
    [
        ("Entrada", "a\nd\na\nr\nt\nn\nE"),
        ("Me gusta la pizza", "a\nz\nz\ni\np\n \na\nl\n \na\nt\ns\nu\ng\n \ne\nM")
    ]
)
def test_revertir_cadena(inCadena_inicial, outReversa_newline):
    assert revertir_cadena(inCadena_inicial) == outReversa_newline

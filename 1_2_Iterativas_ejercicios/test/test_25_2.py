import pytest
from src.Ej_25_2 import la_mas_larga


@pytest.mark.parametrize(
    "inOracion, outPalabraMasLarga",
    [
        ("Erase una vez en un territorio muy muy lejano", "territorio"),
        ("Un video más para perder el tiempo, mi gentes "
        "La canción que todos esperaban "
        "El que quiera perder su tiempo que lo pierda", "esperaban")
    ]
)


def test_la_mas_larga(inOracion, outPalabraMasLarga):
    assert la_mas_larga(inOracion) == outPalabraMasLarga

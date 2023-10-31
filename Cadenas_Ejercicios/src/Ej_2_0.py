"""
Ejercicio 3.0.2¶

Dado que fruta es una variable de tipo cadena, ¿qué significa fruta[:]?
"""


def explicacion_ejercicio(palabra: str) -> str:
    explicacion = (f"Teniendo la palabra {palabra}, sabemos que es una cadena. "
    f"El significado de '{palabra}[:]' es lo mismo,\n"
    f"lo obviamente diferente '[:]' es para aplicar la operación"
    f"'slicing' (rebanado), por la cual se extraen\n"
    f"elementos a la cadena u otras secuencias")
    return explicacion


if __name__ == "__main__":
    # Proceso
    explicado = explicacion_ejercicio("fruta")
    # Salida
    print(explicado)

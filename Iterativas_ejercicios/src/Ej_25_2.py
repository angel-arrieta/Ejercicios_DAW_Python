

"""
Ejercicio 25¶

Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga
(en caso de haber más de una, mostrar la primera) y cuántas palabras había.
Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""

def la_mas_larga(frase: str):  # ;) *guiño*
    respuesta = ""
    frase = frase.split(" ")
    for palabra in frase:
        if len(palabra) > len(respuesta):
            respuesta = palabra
    return respuesta


if __name__ == "__main__":
    frase = str(input("Dime una frase y te dire\n"
    "cual palabra es la mas larga\ny cuantas palabras tiene\n"))
    frase_separada = frase.split(" ")
    cantidad_palabras = len(frase_separada)
    es_grandota = la_mas_larga(frase)
    print(f"Tu frase tiene {cantidad_palabras} palabras y su palabra más larga es: {es_grandota}")

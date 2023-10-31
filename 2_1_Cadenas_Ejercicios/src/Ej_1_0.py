"""
Ejercicio 3.0.1¶

Escribe un bucle while que comience con el último carácter en la
cadena y haga un recorrido hacia atrás hasta el primer carácter
en la cadena, imprimiendo cada letra en una línea independiente.
"""


def revertir_cadena(cadena_inicial: str) -> str:
    cadena_invertida_y_separada = ""
    cadena_inicial = cadena_inicial[::-1]
    posicion = 0
    while posicion < len(cadena_inicial):
        cadena_invertida_y_separada += f"{cadena_inicial[posicion]}\n"
        posicion += 1
    return cadena_invertida_y_separada[:-1]


if __name__ == "__main__":
    try:
        # Entrada
        a_invertir = input("Dime una palabra o frase para invertirla\n> ")
        # Proceso
        cadena_del_reves = revertir_cadena(a_invertir)
        # Salida
        print(cadena_del_reves)
    except ValueError:
        print("El o los valores introducidos, no son un string invertible")

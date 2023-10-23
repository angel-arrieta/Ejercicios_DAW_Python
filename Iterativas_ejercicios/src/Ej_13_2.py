

"""
Ejercicio 13¶

Escribir un programa que muestre el eco de todo lo que el
usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

def resonar(grito):
    return grito


if __name__ == "__main__":
    eco = ""
    # Proceso
    while eco != "salir":
        eco = resonar(str(input("Cámara de eco\t")))  # Entrada
        if eco != "salir":
            # Salida
            print(eco)

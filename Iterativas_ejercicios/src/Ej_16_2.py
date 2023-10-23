

"""
Ejercicio 16¶

Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0.
Informar cuál fue el mayor número ingresado.
"""

def comparador(anterior, actual):
    if actual == 0:
        resultado = "fuera"
    elif actual > anterior:
        resultado = actual
    else:
        resultado = anterior
    return resultado


if __name__ == "__main__":
    ultimo_mayor = 0
    nuevo_a_comparar = 0
    # Entrada
    while nuevo_a_comparar != "fuera":
        ultimo_introducido = int(input("Mete números para comparar\t"))# Proceso
        nuevo_a_comparar = comparador(ultimo_mayor, ultimo_introducido)
        if nuevo_a_comparar != "fuera":
            ultimo_mayor = nuevo_a_comparar
    # Salida
    print(f"{ultimo_mayor} es el número más grande de todos los  introducidos")

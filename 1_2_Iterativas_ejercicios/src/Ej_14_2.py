

"""
Ejercicio 14¶

Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números ingresados.
"""

def sumar(total, actual):
    if actual == 0:
        resultado = "fuera"
    else:
        resultado = total + actual
    return resultado


if __name__ == "__main__":
    sumado = 0
    ultima_suma = 0
    # Proceso
    while ultima_suma != "fuera":
        numero_nuevo = int(input("Mete números para sumar\t")) # Entrada
        ultima_suma = sumar(sumado, numero_nuevo)
        if ultima_suma != "fuera":
            sumado = ultima_suma
    # Salida
    print(f"{sumado} es la suma de todos los números introducidos")

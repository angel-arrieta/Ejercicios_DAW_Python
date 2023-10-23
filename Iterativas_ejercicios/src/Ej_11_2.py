

"""
Ejercicio 11¶

Escribir un programa que pida al usuario una palabra y luego muestre
por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

def recorre_inversa(palabra):
    resultado = ""
    for letra in palabra[::-1]:
        resultado += f"{letra}\n"
    return resultado[:-1]


if __name__ == "__main__":
    # Entrada
    palabra_a_revertir = str(input("Dime una palabra\t"))
    # Proceso
    palabra_invertida = recorre_inversa(palabra_a_revertir)
    # Salida
    print(palabra_invertida)

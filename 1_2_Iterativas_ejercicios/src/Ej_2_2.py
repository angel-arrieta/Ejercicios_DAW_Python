

"""
Ejercicio 2¶

Escribir un programa que pregunte al usuario su edad y muestre
por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def unaVida(edad):
    resultado = ""
    for anos in range(edad):
         resultado += f"{anos + 1}\n"
    return resultado


if __name__ == "__main__":
    # Entrada
    edad = int(input("Introduzca su edad\t"))
    # Proceso
    recorrido_vida = unaVida(edad)
    # Salida
    print(recorrido_vida)

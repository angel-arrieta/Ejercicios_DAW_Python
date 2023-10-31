

"""
Ejercicio 8¶

Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de más abajo.
"""

def escalera(niveles):
    dibujo = ""
    for fila in range(niveles):
        for numero in range((fila+1)*2, 0, -2):
            dibujo += f" {numero-1}"
        dibujo += f"\n"
    return dibujo[:-1]

if __name__ == "__main__":
    # Entrada
    altura = int(input("Dime la altura de la escalera:\t"))
    # Proceso
    triangulo_impares = escalera(altura)
    # Salida
    print(triangulo_impares)


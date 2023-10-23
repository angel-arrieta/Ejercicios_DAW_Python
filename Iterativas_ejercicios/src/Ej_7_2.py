

"""
Ejercicio 7¶

Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
"""

def tablaMultiplicar(numero):
    respuesta = ""
    for n in range(10):
        respuesta += f"{n+1} * {numero} = {(n+1)*numero}\n"
    return respuesta[:-1]


if __name__ == "__main__":
    # Entrada
    multiplo = int(input("Dime de que número quieres tu tabla de multiplicar:\t"))
    # Proceso
    tabla = tablaMultiplicar(multiplo)
    # Salida
    print(tabla)

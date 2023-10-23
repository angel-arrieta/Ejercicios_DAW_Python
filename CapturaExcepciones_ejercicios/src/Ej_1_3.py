
"""
Ejercicio 2.3.1¶

Escribir un programa que pregunte al usuario su edad y muestre por
pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def unaVida(edad: int) -> str:
    resultado = ""
    if edad == 0:
        resultado = "0\n"
    else:
        for anos in range(edad):
            resultado += f"{anos + 1}\n"
    return resultado[:-1]


if __name__ == "__main__":
    edadValida = False
    while not edadValida:
        try:
            # Entrada
            edad_actual = input("Introduzca su edad\t")
            edad_util = int(edad_actual)
            if edad_util < 0:
                raise ValueError
            edadValida = True
        except ValueError:
            print("Por favor, introduzca una edad valida")
    # Proceso
    recorrido_vida = unaVida(edad_util)
    # Salida
    print(recorrido_vida)

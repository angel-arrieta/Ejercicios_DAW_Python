

"""
Ejercicio 10¶

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

def primo(usuario):
    if usuario < 0:
        numero = usuario * -1
    else:
        numero = usuario
    if numero == 1 or numero == 0:
        resultado = f"{usuario} no es primo."
    else:
        comparador = numero - 1
        while comparador > 1:
            resto = numero % comparador
            if resto > 0 and resto != 0:
                comparador -= 1
            elif resto == 0:
                resultado = f"{usuario} no es primo."
                return resultado
        resultado = f"{usuario} es primo."
    return resultado


if __name__ == "__main__":
    # Entrada
    numero = int(input("Dime un numero entero. Te dire si es primo:\t"))
    # Proceso
    afirmacion = primo(numero)
    # Salida
    print(afirmacion)

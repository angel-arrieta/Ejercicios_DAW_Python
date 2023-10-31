

"""
Ejercicio 22¶

Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0.
Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""

def paridad_digitos(numero):
    numero = list(str(numero))
    digitos_pares = 0
    digitos_impares = 0
    for digito in numero:
        if int(digito) % 2 == 1:
            digitos_impares += 1
        else:
            digitos_pares += 1
    return digitos_pares, digitos_impares


if __name__ == "__main__":
    pares = 0
    impares = 0
    numero = 1
    # Proceso
    while numero != 0:
        numero = int(input("Introduzca un numero positivo\t"))  # Entrada
        if numero < 0:
            print("Ingresa un número positivo")
        elif numero == 0:
            continue
        else:
            nuevos_pares, nuevos_impares = paridad_digitos(numero)
            # Salida
            print(f"Tiene {nuevos_pares} digitos pares y {nuevos_impares} digitos impares")
            pares += nuevos_pares
            impares += nuevos_impares
    print(f"En total has introducido {pares} digitos pares y {impares} digitos impares")

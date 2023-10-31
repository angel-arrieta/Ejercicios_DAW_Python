

"""
Ejercicio 24¶

Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1,
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""

def contador_primos(lista):
    primos_encontrados = 0
    for numero in lista:
        comparador = numero - 1
        while comparador > 1:
            resto = numero % comparador
            if resto > 0 and resto != 0:
                comparador -= 1
            elif resto == 0:
                primos_encontrados -= 1
                comparador = 0
        primos_encontrados += 1
    return primos_encontrados


if __name__ == "__main__":
    lista_a_revisar = []
    numero = 1
    # Proceso
    while numero != 0:
        numero = int(input("Dime numeros mayores que 1\n(Ingresa 0 para terminar)\t"))  # Entrada
        if numero > 1:
            lista_a_revisar.append(numero)
        elif numero < 0 or numero == 1:
            print("Numero no registrado")
    primos_encontrados = contador_primos(lista_a_revisar)
    # Salida
    print(f"De los numeros que has ingresado {primos_encontrados} de ellos son primos")

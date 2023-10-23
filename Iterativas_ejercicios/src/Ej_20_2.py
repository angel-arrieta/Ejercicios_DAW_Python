

"""
Ejercicio 20¶

Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide,
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
"""

def buscador_caracteres(frase, letra):
    resultado = ""
    if len(letra) != 1:
        resultado = "Solo una letra"
    else:
        encontrado = frase.find(letra)
        frase = frase[0:encontrado]
        if encontrado == 0:
            resultado = "Encontrado en posición 1"
        else:
            for posicion in range(len(frase)):
                if resultado == "":
                        resultado = "Posiciones donde no esta "
                resultado += f"{posicion+1}, "
            resultado = resultado[:-2] + f". Encontrado en posición {encontrado+1}."
    return resultado


if __name__ == "__main__":
    # Entrada
    oracion = str(input("Dime una frase\n"))
    caracter = str(input("Dime para buscar una letra\t"))
    # Proceso
    encontrado = buscador_caracteres(oracion, caracter)
    # Salida
    print(encontrado)

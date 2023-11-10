"""
Ejercicio 3.0.3¶

Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que
pueda aceptar una cadena y una letra como argumentos.
"""


def cuenta(palabra: str, letra: str) -> int:
    """
    Cuenta cuantas veces aparece la letra en la palabra y
    devuelve el valor de cuanto aparece.
    """
    contador = 0
    palabra = palabra.lower()
    letra = letra.lower()
    for caracter in palabra:
        if caracter == letra:
            contador = contador + 1
    return contador


def control_errores(palabra: str, letra: str) -> int:
    """
    Función que revisa la adecuación de los inputs metidos,
    para que sigan las pautas que el enunciado pide
    --------------
    palabra: str
        cadena a recorrer
    letra: str
        caracter a buscar en la cadena
    return: int
        depende de que incumplan, devuelve un número
        asociado a un error cada uno más importante que otro:
        1 - es una frase, más de una palabra
        2 - la palabra contiene caracteres que no son alfabeticos
        3 - la variable letra es un string vacio
        4 - la variable letra son varios caracteres
        5 - la letra no es un caracter alfabetico
    """
    import re

    fallo = 0
    if re.search(" ", palabra) is not None:
        fallo = 1
        return fallo
    for caracter in palabra:
        if re.search("[A-Za-z]", caracter) is None:
            fallo = 2
            return fallo
    if len(letra) == 0:
        fallo = 3  # Esta vacio
    elif len(letra) > 1:
        fallo = 4  # Son varios carácteres
    elif re.search("[A-Za-z]", letra) is None:
        fallo = 5  # No es una letra
    return fallo


if __name__ == "__main__":
    error = 0
    try:
        # Entrada
        palabra = str(input("Dime una palabra\n> "))
        letra = str(input("Dime una letra a contar en la palabra > "))

        # Proceso
        error = control_errores(palabra, letra)
        if error != 0:
            raise ValueError
        letras_en_palabra = cuenta(palabra, letra)

        # Salida
        print(f"En {palabra} hay {letras_en_palabra} {letra}")

    except ValueError:
        if error == 1:
            print("Solo se permite una palabra")
        elif error == 2:
            print("Solo se permiten letras en la palabra")
        elif error == 3:
            print("Introduce AL MENOS UNA letra")  # Esta vacio
        elif error == 4:
            print("Se permite SOLO UNA letra")  # Es más de un caracter
        elif error == 5:
            print("Se pide una LETRA")  # No es una letra


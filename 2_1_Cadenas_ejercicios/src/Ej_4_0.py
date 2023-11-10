"""
Ejercicio 3.0.4¶

Hay un método de cadenas llamado count que es similar a find.
Lee la documentación de este método y escribe el código necesario para invocar
a este método y contar el número de veces que una letra aparece en “banana”.
"""


def cuenta(palabra: str, letra: str) -> int:
    """
        Cuenta cuantas veces aparece la letra en la palabra y
        devuelve el valor de cuanto aparece.
        """
    veces = 0
    palabra = palabra.lower()
    letra = letra.lower()
    veces += palabra.count(letra)
    return veces


def control_letra(letra: str) -> int:
    """
        Función que revisa la adecuación del input de la letra
        --------------
        letra: str
            caracter a buscar en la cadena
        return: int
            depende de que incumpla, devuelve un número
            asociado a un error cada uno más importante que otro:
            1 - la variable letra es un string vacio
            2 - la variable letra son varios caracteres
            3 - la letra no es un caracter alfabetico
        """
    import re
    fallo = 0
    if len(letra) == 0:
        fallo = 1  # Esta vacio
    elif len(letra) > 1:
        fallo = 2  # Son varios carácteres
    elif re.search("[A-Za-z]", letra) is None:
        fallo = 3  # No es una letra
    return fallo


if __name__ == "__main__":
    error = 0
    palabra = "banana"
    try:
        #  Entrada
        letra = str(input(f"Dime una letra a buscar en {palabra}\n > "))

        #  Proceso
        error = control_letra(letra)
        if error != 0:
            raise ValueError
        veces = cuenta(palabra, letra)

        #  Salida
        print(f"En {palabra} hay {veces} {letra}")

    except ValueError:
        if error == 1:
            print("Introduce AL MENOS UNA letra")  # Esta vacio
        elif error == 2:
            print("Se permite SOLO UNA letra")  # Es más de un caracter
        elif error == 3:
            print("Se pide una LETRA")  # No es una letra

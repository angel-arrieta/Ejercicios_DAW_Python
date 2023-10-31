

"""
Ejercicio 23¶

Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando
el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de
longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea.
Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total
(en todos los títulos de libros que componen en esa línea).
Finalmente, informar cuántas líneas completas se ingresaron.
"""

def cuenta_digitos(linea: list):
    digitos = 0
    for titulo in linea:
        for numero in range(0, 10):
            digitos += titulo.count(str(numero))
    return digitos


def cuenta_lineas(libro: list):
    cantidad = 0
    for linea in libro:
        cantidad += 1
    return cantidad


if __name__ == "__main__":
    linea = []
    registro = []
    nuevo_titulo = ""
    # Proceso
    while nuevo_titulo != "*":
        nuevo_titulo = str(input("Dime títulos de libros"
        " (Introduce / para terminar la \nlinea"
        " ó * para terminar el programa)\n"))
        if nuevo_titulo == "/":
            registro.append(linea)
            digitos = cuenta_digitos(linea)
            print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
            linea = []
        elif nuevo_titulo == "*":
            cantidad_lineas = cuenta_lineas(registro)
        else:
            linea.append(nuevo_titulo)
    print(f"Fin. Se leyeron {cantidad_lineas} líneas completas.")

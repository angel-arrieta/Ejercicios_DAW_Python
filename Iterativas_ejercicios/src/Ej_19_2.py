

"""
Ejercicio 19¶

Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa.
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta,
informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo
volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3,
se interrumpirá la impresión del menú y el programa finalizará.
"""

def menu(opcion):
    if opcion > 3 or opcion < 1:
        resultado = "Opción incorrecta, vuelva a intentar"
    elif opcion == 1:
        resultado = ("""COMENZAR Programa-dolor sit amet, consectetur adipiscing elit.
        Maecenas justo mi, accumsan eu lorem at, ultricies rutrum
        massa. Mauris ac magna vel lorem ultrices tincidunt.
        Nullam vel sem orci. Nullam finibus ex orci. Nullam vitae
        odio sodales, ultricies risus at, imperdiet quam.""")
    elif opcion == 2:
        resultado = (""" IMPRIMIR Listado-dolor sit amet, consectetur adipiscing elit.
         Maecenas justo mi, accumsan eu lorem at, ultricies rutrum
         massa. Mauris ac magna vel lorem ultrices tincidunt.
         Nullam vel sem orci. Nullam finibus ex orci. Nullam vitae
         odio sodales, ultricies risus at, imperdiet quam.""")
    elif opcion == 3:
        resultado = "Saliendo"
    return resultado


if __name__ == "__main__":
    proceso = ""
    # Proceso
    while proceso != "Saliendo":
        # Entrada
        opcion = int(input("""1- comenzar programa
    2- imprimir listado
    3- finalizar programa\n>\t"""))
        proceso = menu(opcion)
        # Salida
        print(proceso)

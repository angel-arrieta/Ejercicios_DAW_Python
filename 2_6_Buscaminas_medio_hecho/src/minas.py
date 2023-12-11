"""
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de los contenidos que
llevamos hasta ahora, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una
responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes
para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

El ejercicio consiste en hacer funcionar el programa resolviendo los problemas que tiene el código. Para ello, se han
añadido comentarios con TODOs que indican qué hay que hacer en cada caso. Además, se han añadido consejos para ayudarte
a resolver los problemas.

Notas importantes que te ayudarán a resolver el ejercicio

- Este código asume un nivel básico de interacción en la consola y no incluye validación exhaustiva de errores de
usuario. No obstante, tú deberías asegurarte de que cualquier error es manejado correctamente.

- Desarrollar la función colocar_minas que tiene la siguiente descripción:

  Esta función coloca las minas en el tablero de juego.
  Se asegura de que el número de minas colocadas sea igual a NUMERO_MINAS.

  Esta función se utiliza en la función generar_tablero.

- Consejo 1: Revisa la función calcular_numeros: depura el programa en la función calcular_numeros porque es
  necesario que soluciones un grave pufo que el programador-becario anterior ha dejado.

- Desarrollar el código de la función contar_minas_adyacentes para que retorne
el número total de minas adyacentes que tiene la celda.

  Ejemplo: la celda (3,3) tiene 3 minas en sus celdas adyacentes...

  1 2 3 4 5 6 7 8
 1  1 2 2 1
 2  1 * * 1
 3  1 3 2 2
 4    1 * 1
 5    1 1 1
 6
 7
 8

  * Ayuda: Puedes usar 2 bucles para recorrer las celdas adyacentes a una celda y acumular las
  minas que encuentres. Pero cuidado con comprobar celdas que estén fuera del rango
  FILAS x COLUMNAS (utiliza las constantes para asegurarte).


- Desarrollar el contenido de la función imprimir_tablero. Podéis usar cómo base la
  función imprimir_tablero_oculto. Analizad dónde se llama a imprimir_tablero y pensad
  bien qué debe mostrar.

  Ten en cuenta que muestra el tablero de juego, no el tablero oculto.

- Consejo 3: Tras hacer un merge, una compañera programadora ha hecho un cambio en la función imprimir_tablero_oculto, y como consecuencia ha dejado de funcionar. Según comenta, antes se usaba la función enumerate dentro de los for (for i, fila in enumerate(tablero):), en vez de range (for fila in range(FILAS):). Revisa la función imprimir_tablero_oculto y corrige el error.

- Consejo 4: Revisa la función pedir_accion y revelar_celda: Nuestro amigo programador-becario dejó otro gran pufo en pedir_accion y
  revelar_celda. Revisa el código y corrige el error.

- Consejo 5: La función marcar_celda no funciona cómo debería... ¿otro regalo de nuestro amigo? Revisa el código y corrige el error.

- Consejo 5: Comprueba por qué no funciona la función jugar()... yo que tú empezaba a depurar.

"""
# Acciones del jugador
MARCAR = "M"
REVELAR = "R"

# Dimensiones del tablero
FILAS = 8
COLUMNAS = 8
NUMERO_MINAS = 10

# Representación del tablero
VACIO = "·"
MINA = "*"
BANDERA = "F"


def generar_tablero() -> list:  # Genera el tablero con las minas puestas
    """
    Esta función genera un tablero de juego vacío y coloca las minas en el tablero. Luego, calcula el número de minas adyacentes a cada celda.
    :return tablero: matriz que actua como tablero de juego del busca minas
    """
    tablero = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    tablero = colocar_minas(tablero, NUMERO_MINAS)
    return tablero


def colocar_minas(tablero: list, cantidad_minas: int) -> list:
    """
    Esta función coloca las minas en el tablero de juego. Se asegura de que el número de minas colocadas sea igual a NUMERO_MINAS.
    :param tablero: tablero de juego
    :param cantidad_minas: minas que se quieren colocar en el tablero
    :return tablero: tablero con las minas colocadas
    """
    import random
    posicion_minas = list()
    for i in range(cantidad_minas):
        seguir = "no"
        while seguir == "no":
            fila = random.randint(0, 7)
            columna = random.randint(0, 7)
            posicion = [fila, columna]
            if posicion_minas.count(posicion) > 0:
                seguir = "no"
            else:
                posicion_minas.append(posicion)
                seguir = "si"
    for mina in posicion_minas:
        tablero[mina[0]][mina[1]] = MINA
    return tablero


def contar_minas_adyacentes(tablero, fila, columna):
    """
    Esta función cuenta el número de minas adyacentes a la celda(i,j) seleccionada.
    :param tablero: tablero de juego
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return conteo_minas: número de minas adyacentes a la celda(i,j) seleccionada
    """
    conteo_minas = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= fila + i < FILAS and 0 <= columna + j < COLUMNAS:
                if (i, j) != (0, 0):
                    if tablero[fila + i][columna + j] == MINA:
                        conteo_minas += 1
    return conteo_minas


def imprimir_tablero(tablero: list) -> str:  # Dibuja el tablero qeu se le pasa
    """
    Esta función toma el tablero como argumento e imprime cada celda del tablero.
    :param tablero: tablero de juego
    :return impresion_tablero: dibujo del tablero de juego
    """
    impresion_tablero = "   1 2 3 4 5 6 7 8\n"
    cantidad_filas_y_columnas = len(tablero)
    for i in range(cantidad_filas_y_columnas):
        fila = " ".join(tablero[i])
        impresion_tablero += f" {i+1} {fila}\n"
    return impresion_tablero


# Primero oculta las minas y le pase el tablero a imprimir_tablero
def imprimir_tablero_oculto(tablero, celdas_marcadas):
    """
    Imprime cada celda del tablero: si la celda ha sido revelada o marcada con una bandera, muestra su contenido actual
    (número, vacio_revelado o bandera); si no, muestra la celda como vacía.
    :param tablero: tablero de juego
    :param celdas_marcadas: celdas con banderas puestas
    :return impresion_oculta: dibujo del tablero sin las minas
    """
    tablero_oculto = list()
    for fila in tablero:
        fila_oculta = list()
        for celda in fila:
            if celda == MINA:
                fila_oculta.append(VACIO)
            else:
                fila_oculta.append(celda)
        tablero_oculto.append(fila_oculta)
    for banderola in celdas_marcadas:
        tablero_oculto[banderola[0]][banderola[1]] = BANDERA

    impresion_oculta = imprimir_tablero(tablero_oculto)
    return impresion_oculta


def pedir_accion():
    """
    Esta función pide al jugador que ingrese una acción, una fila y una columna.
    Si la acción no es válida, se le pide al jugador que ingrese una acción nuevamente.
    Si la fila o la columna no son válidas, se le pide al jugador que ingrese una fila o columna nuevamente.
    :return: acción, fila y columna ingresadas por el jugador

    """
    accion_valida = False
    while not accion_valida:

        accion = input("Elige una acción (R para revelar, M para marcar): ").upper()
        fila = int(input("Ingresa la fila (1-8): ")) - 1
        columna = int(input("Ingresa la columna (1-8): ")) - 1

        if accion in [REVELAR, MARCAR] and 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            accion_valida = True
        else:
            print("Acción inválida. Inténtalo de nuevo.")
    return accion, fila, columna


def revelar_celda(tablero, celdas_reveladas, fila, columna) -> tuple:
    """
    Esta función revela la celda seleccionada.
    Si la celda contiene una mina, devuelve False.
    Si la celda no contiene una mina, se agrega a celdas_reveladas y devuelve True.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return tuple: (celdas_reveladas, tablero, booleano)
            booleano: False si la celda contiene una mina, True en caso contrario
    """
    if tablero[fila][columna] == MINA:  # La celda contiene una mina
        return celdas_reveladas, tablero, False
    else:  # La celda no tiene mina
        celdas_reveladas, tablero = revelar_celdas_vacias(tablero, celdas_reveladas, fila, columna)
        return celdas_reveladas, tablero, True


def revelar_celdas_vacias(tablero, celdas_reveladas, fila, columna):
    """
    Esta función revela la celda seleccionada. Si está vacía, revela recursivamente las celdas vacías adyacentes a la
    celda seleccionada.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    """
    if (fila, columna) not in celdas_reveladas:  # Si la celda no ha sido revelada
        celdas_reveladas.add((fila, columna))
        minas_alrededor = contar_minas_adyacentes(tablero, fila, columna)
        tablero[fila][columna] = f"{minas_alrededor}"
        if minas_alrededor == 0:
            tablero = revelar_alrededor(tablero, fila, columna, 0)
        celdas_reveladas = contar_celdas_reveladas(tablero, celdas_reveladas)
    return celdas_reveladas, tablero


def contar_celdas_reveladas(tablero: list, celdas_reveladas: set) -> set:
    """
    Esta función recoge todas las celdas que han sido reveladas y almacena sus posiciones en un conjunto
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :return celdas_reveladas
    """
    import re
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            if re.search("^[0-7]$", tablero[fila][columna]) is not None:
                celdas_reveladas.add((fila, columna))
    return celdas_reveladas


def revelar_alrededor(tablero, fila, columna, iteracion) -> list:
    """
    Esta función revela las celdas circundantes de una celda que no tiene minas alrededor
    :param tablero: tablero de juego
    :param fila: fila de la celda ya revelada
    :param columna: columna de la celda ya revelada
    :param iteracion: veces que se ha accedido a la recursividad de la propia funcion
    :return tablero:
    """
    celdas = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= fila + i < FILAS and 0 <= columna + j < COLUMNAS:
                if (i, j) != (0, 0):
                    celdas.add((fila + i, columna + j))
    for lugar in celdas:
        cantidad_minas = contar_minas_adyacentes(tablero, lugar[0], lugar[1])
        tablero[lugar[0]][lugar[1]] = f"{cantidad_minas}"
        if iteracion < 2:
            if cantidad_minas == 0:
                tablero = revelar_alrededor(tablero, lugar[0], lugar[1], iteracion+1)
    return tablero


def marcar_celda(celdas_marcadas, fila, columna) -> tuple:
    """
    Esta función marca la celda seleccionada con una bandera.
    :param celdas_marcadas: conjunto de celdas que han sido marcadas con una bandera
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return tuple: (tablero, celdas_marcadas)
    """
    if (fila, columna) not in celdas_marcadas:
        celdas_marcadas.add((fila, columna))
    else:
        celdas_marcadas.discard((fila, columna))
    return celdas_marcadas


def verificar_victoria(ancho: int, cantidad_reveladas: int) -> bool:
    """
    Esta función verifica si el jugador ha ganado el juego. Que se daŕa solo y solo si todas las celdas que no contienen
    minas han sido reveladas.
    :param ancho: ancho del tablero de juego
    :param cantidad_reveladas: cantidad de celdas que ya han sido mostradas al jugador
    :return: True si el jugador ha ganado, False de lo contrario
    """
    victoria = False
    celdas_vacias = (ancho ** 2) - NUMERO_MINAS
    if cantidad_reveladas == celdas_vacias:
        victoria = True
    return victoria


def jugar():
    """
    Función que llama al juego y ejecuta su bucle principal
    """
    tablero = generar_tablero()
    celdas_reveladas = set()
    celdas_marcadas = set()
    terminar_juego = False

    while terminar_juego is False:
        print(imprimir_tablero_oculto(tablero, celdas_marcadas))  # Imprimir tablero sin que se vean las minas
        accion, fila, columna = pedir_accion()

        if accion == "R":
            # Revelar celda
            celdas_reveladas, tablero, celda_con_mina = revelar_celda(tablero, celdas_reveladas, fila, columna)

            if (not celda_con_mina) is True:  # Verificar si has pisado una mina
                print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Oh no! ¡Has pisado una mina!!!!!!!!!!!!!!!!!!!!!")
                print(imprimir_tablero(tablero))
                terminar_juego = True
            if verificar_victoria(len(tablero), len(celdas_reveladas)) is True:  # Verificar si has terminado
                print("¡Felicidades! ¡Has ganado el juego!")
                print(imprimir_tablero(tablero))
                terminar_juego = True
        elif accion == "M":
            celdas_marcadas = marcar_celda(celdas_marcadas, fila, columna)


if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()

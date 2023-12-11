"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""


def jugar(opcion: str) -> str:
    if opcion == "1":
        actuar = "descubrir"
    elif opcion == "2":
        actuar = "marcar"
    elif opcion == "3":
        actuar = "salir"
    else:
        actuar = "error"
    return actuar


def dibujar_tablero(lista_bidimensional: list) -> str:
    tablero_visual = "    0   1   2   3   4   5   6   7\n"
    cantidad_filas_y_columnas = len(lista_bidimensional)
    for i in range(cantidad_filas_y_columnas):
        fila = " ".join(lista_bidimensional[i])
        tablero_visual += f" {i} {fila}\n"
    return tablero_visual[:-1]


def cubrir_tablero(tablero_bid: list) -> list:
    import random
    posicion_minas = []
    for i in range(12):
        seguir = "no"
        while seguir == "no":
            fila = random.randint(0, 7)
            columna = random.randint(0, 7)
            posicion = [fila, columna]
            if posicion_minas.count(posicion) != 0:
                seguir = "no"
            else:
                posicion_minas.append(posicion)
                seguir = "si"
    tablero_dispuesto = tablero_bid.copy()
    for mina in posicion_minas:
        fila_mina, col_mina = mina[1], mina[0]
        tablero_dispuesto[fila_mina][col_mina] = "[*]"
    return tablero_dispuesto


def control_coordenada(coordenadas: str) -> int:
    coordenadas = coordenadas.strip()
    fallo = 0
    import re
    if coordenadas.count(",") != 1:
        fallo = 2
    elif re.search("^[0-7],[0-7]$", coordenadas) is None:
        fallo = 3
    return fallo


def comprobar_celda(campo_real: list, posicion: list) -> bool:
    fila, columna = posicion[0], posicion[1]
    celda = campo_real[fila][columna]
    if celda == "[*]":
        mina = True
    else:
        mina = False
    return mina


def marcar_celda(campo: list, posicion: list, cambio: str) -> list:
    fila, columna = posicion[0], posicion[1]
    campo[fila][columna] = f"[{cambio}]"
    return campo


def revelar_celda(campo_real: list, posicion: list, iteracion: int) -> list:
    fila, columna = posicion[0], posicion[1]
    if fila == 0:
        if fila == 0 and columna == 0:
            celdas_circundantes = [
                campo_real[fila][columna + 1], campo_real[fila + 1][columna], campo_real[fila+1][columna+1] ]
        elif fila == 0 and columna == 7:
            celdas_circundantes = [
                campo_real[fila][columna - 1], campo_real[fila + 1][columna], campo_real[fila+1][columna-1] ]
        else:
            celdas_circundantes = [
                campo_real[fila][columna - 1], campo_real[fila][columna + 1], campo_real[fila + 1][columna - 1],
                campo_real[fila + 1][columna], campo_real[fila + 1][columna + 1] ]
    elif fila == 7:
        if fila == 7 and columna == 0:
            celdas_circundantes = [
                campo_real[fila - 1][columna], campo_real[fila - 1][columna + 1], campo_real[fila][columna + 1] ]
        elif fila == 7 and columna == 7:
            celdas_circundantes = [
                campo_real[fila - 1][columna], campo_real[fila - 1][columna - 1], campo_real[fila][columna - 1] ]
        else:
            celdas_circundantes = [
                campo_real[fila - 1][columna - 1], campo_real[fila - 1][columna], campo_real[fila - 1][columna + 1],
                campo_real[fila][columna - 1], campo_real[fila][columna + 1] ]
    elif columna == 0:
        celdas_circundantes = [
            campo_real[fila - 1][columna], campo_real[fila - 1][columna + 1], campo_real[fila][columna + 1],
            campo_real[fila + 1][columna], campo_real[fila + 1][columna + 1] ]
    elif columna == 7:
        celdas_circundantes = [
            campo_real[fila - 1][columna - 1], campo_real[fila - 1][columna], campo_real[fila][columna - 1],
            campo_real[fila + 1][columna - 1], campo_real[fila + 1][columna] ]
    else:
        celdas_circundantes = [
            campo_real[fila-1][columna-1], campo_real[fila-1][columna], campo_real[fila-1][columna+1],
            campo_real[fila][columna-1], campo_real[fila][columna+1],
            campo_real[fila+1][columna-1], campo_real[fila+1][columna], campo_real[fila+1][columna+1]
            ]
    alrededor = celdas_circundantes.count("[*]")
    if alrededor != 0:
        campo_real[fila][columna] = f"[{alrededor}]"
    else:
        campo_real[fila][columna] = f"[0]"
        if iteracion == 0:
            if fila == 0:
                if fila == 0 and columna == 0:
                    alrededores = [[fila, columna + 1], [fila + 1, columna], [fila + 1, columna + 1]]
                elif fila == 0 and columna == 7:
                    alrededores = [[fila, columna - 1], [fila + 1, columna - 1], [fila + 1, columna]]
                else:
                    alrededores = [[fila, columna - 1], [fila, columna + 1],
                                   [fila + 1, columna - 1], [fila + 1, columna], [fila + 1, columna + 1]]
            elif fila == 7:
                if fila == 7 and columna == 0:
                    alrededores = [[fila - 1, columna], [fila - 1, columna + 1], [fila, columna + 1]]
                elif fila == 7 and columna == 7:
                    alrededores = [[fila - 1, columna - 1], [fila - 1, columna], [fila, columna - 1]]
                else:
                    alrededores = [[fila - 1, columna - 1], [fila - 1, columna], [fila - 1, columna + 1],
                                   [fila, columna - 1], [fila, columna + 1]]
            elif columna == 0:
                alrededores = [[fila - 1, columna], [fila - 1, columna + 1], [fila, columna + 1],
                               [fila + 1, columna], [fila + 1, columna + 1]]
            elif columna == 7:
                alrededores = [[fila - 1, columna - 1], [fila - 1, columna], [fila, columna - 1],
                               [fila + 1, columna - 1], [fila + 1, columna]]
            else:
                alrededores = [[fila - 1, columna - 1], [fila - 1, columna], [fila - 1, columna + 1],
                               [fila, columna - 1], [fila, columna + 1],
                               [fila + 1, columna - 1], [fila + 1, columna], [fila + 1, columna + 1]]
            campo_vista = campo_real.copy()
            for sitio in alrededores:
                campo_vista = revelar_celda(campo_real, sitio, iteracion+1)
            campo_real = campo_vista
    return campo_real


def cubrir_minas(campo_descubierto: list) -> list:
    campo_cubierto = list()
    for fila in campo_descubierto:
        nueva_fila = list()
        for hueco in fila:
            if hueco == "[*]":
                nueva_fila.append("[ ]")
            else:
                nueva_fila.append(hueco)
        campo_cubierto.append(nueva_fila)
    return campo_cubierto


def input_posicion_usable(coordenadas: str) -> list:
    usable = list()
    posiciones = coordenadas.strip().split(",")
    for posicion in posiciones:
        usable.append(int(posicion))
    return usable


def crear_tablero() -> list:
    tabla = list()
    for i in range(8):
        fila = list()
        for n in range(8):
            fila.append("[ ]")
        tabla.append(fila)
    return tabla


def verificacion_victoria(tablero: list) -> str:
    huecos = 0
    for fila in tablero:
        for celda in fila:
            if celda == "[ ]":
                huecos += 1
    if huecos == 0:
        return "gana"
    return "nada"


if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    salir = "no"
    estado_jugador = "nada"
    error = 0
    tablero_visual = crear_tablero()
    minas = 12
    tabla = crear_tablero()
    tablero_real = cubrir_tablero(tabla)
    # Proceso
    while salir == "no":
        try:
            visualizar_tablero = dibujar_tablero(tablero_visual)
            print(visualizar_tablero)
            # Entrada
            accion = (input("Elige una acción:\n"
                               "1. Descubrir celda\n"
                               "2. Marcar celda\n"
                               "3. Salir\n"
                               f"Minas: {minas}\n\n"
                               "Tu elección: "))
            decision = jugar(accion)
            if decision == "error":
                error = 1
                raise ValueError(error)
            else:
                if decision == "salir":
                    salir = "si"
                else:
                    # Entrada
                    lugar = str(input("Ingresa coordenadas (fila,columna):\t"))
                    error = control_coordenada(lugar)
                    if error != 0:
                        raise ValueError(error)
                    else:
                        celda = input_posicion_usable(lugar)
                        if decision == "marcar":
                            tablero_visual = marcar_celda(tablero_visual, celda, "B")
                            minas -= 1
                        elif decision == "descubrir":
                            booleano_mina = comprobar_celda(tablero_real, celda)
                            if booleano_mina is True:  # Pierde
                                tablero_perdido = marcar_celda(tablero_real, celda, "X")
                                estado_jugador = "pierde"
                                salir = "si"
                            else:  # Sigue
                                tablero_real = revelar_celda(tablero_real, celda, 0)
                                estado_jugador = verificacion_victoria(tablero_real)
                                tablero_intermedio = tablero_real.copy()
                                tablero_visual = cubrir_minas(tablero_intermedio)
                            # Pierde o Gana
                            if estado_jugador != "nada":
                                salir = "si"

        except ValueError:
            if error == 1:
                print("Opción de acción no reconocida")
            elif error == 2:
                print("Comas de la coordenada mal introducida: Formato aceptado: [0-7],[0-7]")
            elif error == 3:
                print("Formato de la coordenada mal introducido: Formato aceptado: [0-7],[0-7]")
    # Salida
    if estado_jugador != "nada":
        if estado_jugador == "pierde":
            tablero_perdido = dibujar_tablero(tablero_perdido)
            print("         Has perdido\n"
                  f"{tablero_perdido}")
        elif estado_jugador == "gana":
            tablero_resuelto = dibujar_tablero(tablero_real)
            print("         ¡ Has ganado !\n"
                  f"{tablero_resuelto}")

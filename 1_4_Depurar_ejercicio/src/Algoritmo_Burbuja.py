def algoritmo_burbuja(lista: list) -> list:
    revisiones_realizadas = 0
    for veces in range(len(lista) - 1):
        for actual in range(len(lista) - revisiones_realizadas):
            if lista.index(lista[actual]) == len(lista)-1:
                continue
            else:
                siguiente = lista[actual+1]
                if lista[actual] < siguiente:
                    continue
                elif lista[actual] > siguiente:
                    segundo = lista[actual]
                    lista[actual] = lista[actual + 1]
                    lista[actual + 1] = segundo
        revisiones_realizadas += 1
    return lista


if __name__ == "__main__":
    listado = [8, 3, 1, 19, 14]
    try:
        try:
            for numero in listado:
                if type(numero) != int:
                    listado[listado.index(numero)] = int(numero)
                else:
                    continue
        except ValueError:
            print("Un valor de la lista no es número entero")
            raise ValueError
        # Proceso
        procesado = algoritmo_burbuja(listado)
        # Salida
        print(procesado)
    except ValueError:
        print("No se puede ejecutar el algoritmo")
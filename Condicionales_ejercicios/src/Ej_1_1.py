def Comprobacion_edad(edad):
    respuesta = "Error al introducir la edad"
    if edad <= 0:
        respuesta = "Error al introducir la edad"
    elif edad < 18 and edad > 0:
        respuesta = "Es menor de edad"
    elif edad >= 18:
        respuesta = "Es mayor de edad"
    return respuesta


if __name__ == "__main__":
    print(Comprobacion_edad(int(input("Introduzca su edad:  "))))

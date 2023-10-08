def nombrar(nombre, cantidad):
    respuesta = ""
    while cantidad > 0 :
        respuesta += f"{nombre}\n"
        cantidad -= 1
    return respuesta


if __name__ == "__main__":
    print(nombrar(str(input("Dime tu nombre: ")),int(input("Dime un número sin decimales: "))))

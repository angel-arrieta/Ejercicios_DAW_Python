def telefono(numero):
    return f"El número original es {numero[3:12]}"


if __name__ == "__main__":
    print(telefono((str(input("Introduzca un número en formato prefijo-número-extension [+XX-(9X)-XX]\n")))))

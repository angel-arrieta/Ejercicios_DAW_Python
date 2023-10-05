def bienvenida(usuario):
    return f"Hola, {usuario}"


if __name__ == "__main__":
    nombre = str(input("Escribe tu nombre:  "))
    print(bienvenida(nombre))

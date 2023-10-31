def suman(uno, dos):
    return uno + dos


def sumar(uno, dos):
    return f"El resultado da {uno + dos}"


if __name__ == "__main__":
    uno = float(input("Introduce un número: "))
    dos = float(input("Introduce otro número: "))
    uno = suman(uno, dos)
    tres = float(input("Introduce otro número más: "))
    print(sumar(uno, tres))

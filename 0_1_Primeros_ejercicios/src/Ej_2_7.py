def sumar(uno, dos, tres):
    return f"El resultado da {uno + dos + tres}"


if __name__ == "__main__":
    uno = float(input("Introduce un número: "))
    dos = float(input("Introduce otro número: "))
    tres = float(input("Introduce otro número más: "))
    print(sumar(uno, dos, tres))

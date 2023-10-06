def sumar(uno, dos, tres):
    return f"El resultado da {uno + dos + tres}"


if __name__ == "__main__":
    print(sumar(float(input("Introduce un número: ")), float(input("Introduce otro número: ")), float(input("Introduce otro número más: "))))
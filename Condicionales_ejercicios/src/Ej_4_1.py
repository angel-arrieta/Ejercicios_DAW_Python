def paridad(numero):
    if numero % 2 == 1:
        veracidad = "Tu número es impar"
    elif numero % 2 == 0:
        veracidad = "Tu número es par"
    return veracidad


if __name__ == "__main__":
    print(paridad(int(input("Dime un número, te dire si es par o impar:\t"))))

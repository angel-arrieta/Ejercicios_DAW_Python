def division(primero, segundo):
    if segundo == 0:
        resultado = "Error, la operación es indivisible"
    else:
        resultado = str(primero/segundo)
    return resultado


if __name__ == "__main__":
    print("Vamos a dividir")
    print(division(int(input("Introduce el dividendo:  ")),int(input("Introduce el divisor:  "))))


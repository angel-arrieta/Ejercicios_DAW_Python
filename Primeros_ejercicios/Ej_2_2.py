def importe(hora, coste):
    return f"Importe total: {hora * coste}"


if __name__ == "__main__":
    horas = int(input("Horas de trabajo: "))
    coste = int(input("Coste por hora: "))
    print(importe(horas, coste))

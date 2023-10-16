def comprobar_tributar(edad, ingreso):
    if edad > 16 and ingreso >= 1000:
        resultado = "Usted debe tributar"
    else:
        resultado = "Usted no debe tributar"
    return resultado


if __name__ == "__main__":
    print(comprobar_tributar(int(input("Introduzca su edad:\t")), int(input("Intoduzca sus ingresos:\n"))))

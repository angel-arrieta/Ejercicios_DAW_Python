def declaracion(renta):
    if 0 < renta < 10000:
        resultado = "Su renta anual es del 5%"
    elif 10000 <= renta < 20000:
        resultado = "Su renta anual es del 15%"
    elif 20000 <= renta < 35000:
        resultado = "Su renta anual es del 20%"
    elif 35000 <= renta < 60000:
        resultado = "Su renta anual es del 30%"
    elif renta >= 60000:
        resultado = "Su renta anual es del 45%"
    elif renta <= 0:
        resultado = "Valor de renta sin sentido"
    return resultado


if __name__ == "__main__":
    print(declaracion(int(input("Introduzca su renta anual\n"))))

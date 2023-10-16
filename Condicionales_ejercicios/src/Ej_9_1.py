def entrada(edad):
    if 0 < edad <= 4:
        resultado = "¿A que esperas? ¡Entra adentro, chic@!"
    elif 4 < edad < 18:
        resultado = "¡Por 5 euros puedes entrar, chaval!"
    elif 18 <= edad < 25:
        resultado = "Por solo 10 euros puede entrar, jovencit@"
    elif edad >= 25:
        resultado = "Buenas señor/a debe pagar 10 euros por la entrada"
    else:
        resultado = "Perdona, pero no lo entendi bien"
    return resultado


if __name__ == "__main__":
    print(entrada(int(input("Bienvenido a Fazbear Entertainment\nIntroduzca su edad:\t"))))

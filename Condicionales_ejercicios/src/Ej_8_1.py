def evaluacion(puntuacion):
    if puntuacion == 0.0:
        resultado = "Evaluación inaceptable, sin bonificación obtenida"
    elif puntuacion == 0.4:
        resultado = f"Evaluación aceptable, bonificación de {0.4 * 2400} obtenida"
    elif puntuacion >= 0.6:
        resultado = f"Evaluación meritoria obtenida, bonificación de {puntuacion * 2400}"
    else:
        resultado = "Datos Introducidos ilegibles o incorrectos"
    return resultado


if __name__ == "__main__":
    print(evaluacion(float(input("Introducir Evaluación Anual\n"))))

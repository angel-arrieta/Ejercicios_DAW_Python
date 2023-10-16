def division(sexo, nombre):
    mujer = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    hombre = mujer
    inicial = (nombre.lower())[0]
    hombre.append("n")
    if sexo == "hombre":
        if inicial in hombre:
            resultado = "Estas en el grupo B"
        else:
            resultado = "Estas en el grupo A"
    elif sexo == "mujer":
        if inicial in mujer:
            resultado = "Estas en el grupo A"
        else:
            resultado = "Estas en el grupo B"
    elif sexo != "hombre" and sexo != "mujer":
        resultado = "Datos introducidos incorrectamente"
    return resultado


if __name__ == "__main__":
    print(division(str(input("¿Eres hombre o mujer?\t"), str(input("Escribe tu nombre\t")))))

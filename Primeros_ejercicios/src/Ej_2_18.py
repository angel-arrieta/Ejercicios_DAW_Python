def nombreCompleto(nombreCompleto):

    nombreMinuscula = nombreCompleto.lower()
    nombreMayuscula = nombreCompleto.upper()
    nombrePrimeraMayuscula = nombreCompleto.title()
    return f"{nombreMinuscula}, {nombreMayuscula}, {nombrePrimeraMayuscula}"


if __name__ == "__main__":
    nombre = str(input("¿Cual es tu nombre completo?\n"))
    print(nombreCompleto(nombre))
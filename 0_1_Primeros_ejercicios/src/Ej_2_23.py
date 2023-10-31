def cambio_dominio(correo):
    correo = correo.split('@', 1)[0]
    return correo + "@ceu.es"


if __name__ == "__main__":
    print(cambio_dominio(str(input("Introduzca su correo:\n"))))

def Comprueba_contrasena(intento_usuario):
    contrasena = "contraseña"
    if intento_usuario == contrasena:
        respuesta = "Contraseña correcta"
    else:
        respuesta = "Contraseña equivocada"
    return respuesta


if __name__ == "__main__":
    print(Comprueba_contrasena(str(input("Introduzca la contraseña:\n"))))

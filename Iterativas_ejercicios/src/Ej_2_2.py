def unaVida(edad):
    resultado = ""
    for anos in range(edad):
         resultado += f"{anos + 1}\n"
    return resultado


if __name__ == "__main__":
    print(unaVida(int(input("Introduzca su edad\t"))))

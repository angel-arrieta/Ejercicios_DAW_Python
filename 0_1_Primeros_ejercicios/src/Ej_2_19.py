def contar(nombre):
    return f"Tiene {len(nombre)} letras"


if __name__ == "__main__":
    print(contar(str(input("¿Cúal es tu nombre?\t"))))

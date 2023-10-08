def mayusculizar(frase, letra):
    return f"{frase.replace(letra.lower(),letra.upper())}"


if __name__ == "__main__":
    print(mayusculizar(str(input("Dime una frase: ")), str(input("Dime una vocal a cambiar a Mayúscula: "))))

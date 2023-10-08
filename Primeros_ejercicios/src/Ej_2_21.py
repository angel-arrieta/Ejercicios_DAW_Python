def invertir(frase):
    return f"{frase[::-1]}"


if __name__ == "__main__":
    print(invertir(str(input("Introduce una frase a invertir\n"))))

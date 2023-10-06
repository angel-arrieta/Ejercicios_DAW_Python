def sumatorio(num):
    return f"El sumatorio de {num} es {num * (num +1) / 2}"


if __name__ == "__maim__":
    print(sumatorio(float((input("Introduce un número para hacer\t su sumatorio (1 + 2 + 3 +...+ n): ")))))
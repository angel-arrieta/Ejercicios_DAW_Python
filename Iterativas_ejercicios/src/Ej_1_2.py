def decamultiplicador(palabra):
    multiplicado = ""
    for x in range(10):
        multiplicado += f"{palabra}\n"
    return multiplicado


if __name__ == "__main__":
    print(decamultiplicador(str(input("Vale del Décimo Eco ¡Grita una palabra!\t"))))

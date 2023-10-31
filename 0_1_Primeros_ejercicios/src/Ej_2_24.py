def desglose(precio):
    unidades = round(precio, 2)//1
    return f"El artículo vale {int(unidades)} euros y {int((precio-unidades)*100)} centimos"


if __name__ == "__main__":
    print(desglose(float(input("Introduzca el precio de un producto: "))))

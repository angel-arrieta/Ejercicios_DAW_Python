def peso_paquete(payasos, munecas):
    return f"El paquete pesa {(payasos * 112 + munecas * 75) / 100} kilogramos"


if __name__ == "__main__":
    print(peso_paquete(int(input("Introduce los payasos del pedido: ")),int(input("Introduce las muñecas del pedido: "))))

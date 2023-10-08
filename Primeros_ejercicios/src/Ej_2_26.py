def lista_compra(productos):
    lista_de_productos = productos.split(",")
    return "\n".join(lista_de_productos)


if __name__ == "__main__":
    print(lista_compra(str(input("Introduce los productos de tu lista de la compra separado por comas:\n"))))

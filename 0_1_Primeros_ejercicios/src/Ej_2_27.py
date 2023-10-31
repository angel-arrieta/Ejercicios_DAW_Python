def calculadora_producto(producto, precio, cantidad):
    return (f"{producto} vale {precio:09.2f}\n"
    f"{cantidad:03d} {producto} vale {precio * cantidad:011.2f}")


if __name__ == "__main__":
    print(calculadora_producto((input("Producto a comprar: ")),float(input("Precio del producto: ")),int(input("Cantidad del producto: "))))

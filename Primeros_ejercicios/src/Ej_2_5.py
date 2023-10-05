def calcular_iva(articulo, impuesto):
    return f"El precio con IVA es {articulo + articulo / 100 * impuesto}"


if __name__ == "__main__":
    articulo = float(input("Dime el precio del producto: "))
    impuesto = float(input("Dime el impuesto a añadir: "))
    print(calcular_iva(articulo, impuesto))
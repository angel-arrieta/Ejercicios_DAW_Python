def sustraer_iva(precio_final):
    return f"El precio inicial es {precio_final / 110 * 100}"


if __name__ == "__main__":
    print(sustraer_iva(float(input("Dime el precio final del producto (IVA 10% aplicado): "))))

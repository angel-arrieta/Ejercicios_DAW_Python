def barras_pasadas(cantidad):
    return (f"Cada barra se vende a 3.49 euros, sí no es fresca se le descuenta un 60½\n"
    f"Se ha conseguido {round((3.49 * 0.6 * cantidad), 2)} euros de barras que no son del día")


if __name__ == "__main__":
    print(barras_pasadas(int(input("Introduce las barras vendidad que no son del día: "))))

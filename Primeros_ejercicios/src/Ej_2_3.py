def cuentas(ancho, alto):
    return (f"""1. {ancho / 2}
    2. {ancho // 2}
    3. {alto / 3}
    4. {1 + 2 * 5} """)


if __name__ == "__main__":
    ancho = 17
    alto = 12.0
    print(cuentas(ancho, alto))

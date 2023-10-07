def div_por_partes(n, m):
    return f"la división de {n} entre {m} da un cociente {n//m} y un resto {n%m}"


if __name__ == "__main__":
    print(div_por_partes(float(input("Introduce un número a dividir: ")),float(input("Introduce un número que divida: "))))

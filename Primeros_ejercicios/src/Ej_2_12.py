def calculadora_imc(peso, estatura):
    return f"Tú índice de masa corporal es {peso / estatura**2}"


if __name__ == "__maim__":
    peso = float(input("Introduce tu peso en kilogramos: "))
    estatura = float(input("Introduce tu estaura en metros: "))
    print(calculadora_imc(peso, estatura))

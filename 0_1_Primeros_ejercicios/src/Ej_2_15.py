def intereses(balance):
    primer_ano = balance * 1.04
    segundo_ano = primer_ano * 1.04
    tercer_ano = segundo_ano * 1.04
    return (f"El primer año acabas con {round(primer_ano, 2)} euros\n"
    f"El segundo año acabas con {round(segundo_ano, 2)} euros\n"
    f"El tercer año acabas con {round(tercer_ano, 2)} euros")


if __name__ == "__main__":
    print(intereses(float(input("Introduce el balance de tu cuenta\n(Interés ofrecido del 4%): "))))

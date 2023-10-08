def fechado(fecha):
    dia = fecha[:-8]
    mes = (int(fecha[:-5][-2:])) - 1
    ano = fecha[-4:]
    lista_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                "noviembre", "diciembre"]
    mes_escrito = lista_meses[mes]
    return f"Usted nacio el {dia} de {mes_escrito} del año {ano}"


if __name__ == "__main__":
    print(fechado(str(input("Introduzca su fecha de nacimiento (formato dd/mm/aaaa)\n"))))

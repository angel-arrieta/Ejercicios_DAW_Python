def menu(afirmacion):
    if afirmacion == "si":
        menu = ["pimiento", "tofu"]
    elif afirmacion == "no":
        menu = ["pimiento", "tofu", "peperoni", "jamón", "salmón"]
    else:
        menu = "Error"
    return menu


def anadir(menu, ingrediente):
    if ingrediente in menu:
        menu.remove(ingrediente)
        resultado = menu, ingrediente
    elif ingrediente not in menu:
        if ingrediente == "salir":
            resultado = "fuera"
        else:
            resultado = "no_hay"
    return resultado


def comanda(pizza, preferencia):
    componentes = ""
    if preferencia == "si":
        tipo = "vegetariana "
    else:
        tipo = ""
    for ingrediente in pizza:
        componentes += f"{ingrediente}, "
    componentes = componentes[:-2]
    return tipo, componentes


if __name__ == "__main__":
    pizza = ["tomate", "queso"]
    preferencia = str(input("Bienvenidos a la pizzeria Bella Napoli\n¿Es usted vegetariano o no? (si/no)\t"))
    opciones = menu(preferencia.lower())
    if type(opciones) == type(["referencia"]):
        while opciones != []:
            print(opciones)
            respuesta = anadir(opciones, (str(input("Escoja un ingrediente (Introduce 'salir' para terminar)\t"))).lower())
            if type(respuesta) == type(("ref","ref")):
                opciones, ingrediente = respuesta
                pizza.append(ingrediente)
            else:
                if respuesta == "fuera":
                    break
                print("El ingrediente no existe o se ha acabado")
        tipo, componentes = comanda(pizza, preferencia)
        print(f"Has pedido una pizza {tipo}con {componentes}")
    else:
        print("Aclaración mal introducida")

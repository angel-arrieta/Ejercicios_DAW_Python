

"""
Ejercicio 21¶

Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo,
no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total
a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar
un 10% de descuento.
"""

def compra(total_venta, ultimo_precio):
    if ultimo_precio < 0:
        resultado = total_venta
    else:
        resultado = total_venta + ultimo_precio
    return resultado


def descuento(pedido):
    if pedido >= 1000:
        resultado = pedido - (pedido/100*10)
    else:
        resultado = pedido
    return resultado


if __name__ == "__main__":
    total_compra = -1
    ultimo_monto = 1
    # Proceso
    while ultimo_monto != 0:
        total_compra = compra(total_compra, ultimo_monto)
        ultimo_monto = int(input("Ingresa los precios de los productos a comprar\n"
        "(Si la compra supera más de $1000 se aplica un 10% de descuento)\n"
        "(Ingrese 0 para terminar)\t"))  # Entrada
        if ultimo_monto < 0:
            print("Ingrese otro monto")
    total_compra = descuento(total_compra)
    # Salida
    print(f"Total a pagar: {total_compra}")


"""
Ejercicio 2.3.3¶

Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
Deberá solicitar el número hasta introducir uno correcto.
"""

def cuentaAtras(inicio: int) -> str:
    resultado = ""
    for n in range(inicio, -1, -1):
        resultado += f"{n}, "
    return resultado[:-2]


if __name__ == "__main__":
    inicioValido = False
    while not inicioValido:
        try:
            # Entrada
            primer_numero = input("¿Desde que número comenzamos la cuenta atras?\t")
            primero_util = int(primer_numero)
            if primero_util < 1:
                raise ValueError
            inicioValido = True
        except ValueError:
            print("Introduzca un inicio de cuenta lógico")
    # Proceso
    cuenta_regresiva = cuentaAtras(primero_util)
    # Salida
    print(cuenta_regresiva)

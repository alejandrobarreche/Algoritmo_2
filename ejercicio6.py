def calcular_descuento(cantidad_componentes, cliente):
    # Calcular el descuento basado en la cantidad de componentes pedidos
    if 10000 <= cantidad_componentes <= 20000:
        descuento = 0.10
    elif 20001 <= cantidad_componentes <= 40000:
        descuento = 0.15
    elif cantidad_componentes > 40000:
        descuento = 0.20
    else:
        descuento = 0

    # Ajustar el descuento según el cliente
    if cliente == "COMMAQ":
        descuento -= 0.02
    elif cliente == "BEL":
        descuento += 0.01

    return descuento

def main():
    print("Este programa calcula el porcentaje de descuento concedido para un pedido de microprocesadores.")

    try:
        # Solicitar la cantidad de componentes y el cliente al usuario
        cantidad_componentes_pedidos = int(input("Ingrese la cantidad de componentes pedidos: "))
        cliente = input("Ingrese el nombre del cliente (COMMAQ o BEL): ").upper()
        if cliente not in ["COMMAQ", "BEL"]:
            raise ValueError("Cliente no válido. Por favor, ingrese COMMAQ o BEL.")

        # Calcular el descuento
        descuento = round(calcular_descuento(cantidad_componentes_pedidos, cliente),2)

        # Imprimir el descuento
        print("El porcentaje de descuento concedido es:", descuento * 100, "%")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

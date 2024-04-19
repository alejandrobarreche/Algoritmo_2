def calcular_descuento(num_ninos):
    if num_ninos < 2:
        descuento = 0
    elif num_ninos == 2:
        descuento = 0.10
    elif num_ninos == 3:
        descuento = 0.15
    elif num_ninos == 4:
        descuento = 0.18
    elif num_ninos >= 5:
        descuento = 0.18 + ((num_ninos - 4) * 0.01)
    else:
        raise ValueError("El número de niños debe ser mayor o igual a 0.")
    
    return descuento

def main():
    print("Este programa calcula el descuento aplicable según el número de niños en la familia.")

    try:
        # Solicitar el número de niños al usuario
        num_ninos_familia = int(input("Ingrese el número de niños en la familia: "))
        if num_ninos_familia < 0:
            raise ValueError("El número de niños debe ser mayor o igual a 0.")

        # Calcular el descuento
        descuento = calcular_descuento(num_ninos_familia)

        # Imprimir el descuento
        print("El importe del descuento es:", descuento * 100, "%")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

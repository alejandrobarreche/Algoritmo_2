def calcular_descuento(importe):
    if importe <= 0:
        raise ValueError("El importe de la compra debe ser mayor que cero.")
    elif 0 < importe < 100:
        descuento = 0
    elif 100 <= importe <= 500:
        descuento = importe * 0.05
    else:
        descuento = importe * 0.08
    return descuento

def main():
    print("Este programa calcula el descuento aplicable a una compra.")

    try:
        importe_compra = float(input("Ingrese el importe de la compra: "))

        descuento = round(calcular_descuento(importe_compra),2)
        print(f"El descuento que se le ha aplicado es de {descuento} €. \nEl precio final es de {importe_compra - descuento} €")
    except ValueError:
        print("Por favor, ingrese un importe válido.")

if __name__ == "__main__":
    main()

def calcular_prima_anual(kilometros_recorridos, antiguedad, accidentes):
    # Calculamos la prima de distancia
    prima_distancia = min(kilometros_recorridos * 0.01, 400)

    # Calculamos la prima de antigüedad
    prima_antiguedad = 0
    if antiguedad >= 4:
        prima_antiguedad = 200 + (antiguedad - 4) * 20

    # Determinamos la prima total según el número de accidentes
    if accidentes == 0 or accidentes < 3:
        prima_total = prima_distancia + prima_antiguedad
    elif accidentes == 1:
        prima_total = (prima_distancia + prima_antiguedad) / 2
    elif accidentes == 2:
        prima_total = (prima_distancia + prima_antiguedad) / 3
    elif accidentes == 3:
        prima_total = (prima_distancia + prima_antiguedad) / 4
    else:
        prima_total = 0

    return prima_total

def main():
    print("Este programa calcula la prima anual para los conductores de LA CAMPANA.")

    try:
        # Solicitar los datos al usuario
        kilometros_recorridos = float(input("Ingrese los kilómetros recorridos durante el año: "))
        antiguedad = int(input("Ingrese los años de antigüedad del conductor: "))
        accidentes = int(input("Ingrese el número de accidentes durante el año: "))

        # Calcular la prima anual
        prima = calcular_prima_anual(kilometros_recorridos, antiguedad, accidentes)

        # Imprimir el resultado
        print("La prima anual que se concederá al conductor es:", round(prima, 2), "€")
    except ValueError:
        print("Error: Por favor, ingrese datos válidos.")

if __name__ == "__main__":
    main()

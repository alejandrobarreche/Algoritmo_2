def calcular_coste_viaje(num_alumnos):
    # Calcular el coste del trayecto
    if num_alumnos <= 25:
        coste_trayecto = 67.30
    else:
        coste_trayecto = 61.00

    # Calcular el coste de la comida
    coste_comida = 3.50 * num_alumnos

    # Calcular el coste del alojamiento
    if num_alumnos < 30:
        coste_alojamiento = 4.75 * num_alumnos
    elif 30 <= num_alumnos <= 35:
        coste_alojamiento = 4.00 * num_alumnos
    else:
        coste_alojamiento = 3.50 * num_alumnos

    # Calcular el coste total y el coste por alumno
    coste_total = coste_trayecto + coste_comida + coste_alojamiento
    coste_por_alumno = coste_total / num_alumnos

    return coste_por_alumno, coste_total

def main():
    print("Este programa calcula el coste por alumno y el coste total de un viaje escolar.")

    try:
        # Solicitar la cantidad de alumnos al usuario
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos que participarán en el viaje: "))
        if cantidad_alumnos <= 0:
            raise ValueError("La cantidad de alumnos debe ser un número positivo.")

        # Calcular el coste del viaje
        coste_por_alumno, coste_total = calcular_coste_viaje(cantidad_alumnos)

        # Imprimir el resultado
        print("El coste por alumno es:", round(coste_por_alumno, 2), "€")
        print("El coste total del viaje es:", round(coste_total, 2), "€")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

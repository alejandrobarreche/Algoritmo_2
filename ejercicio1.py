from datetime import datetime, timedelta



def dia_semana(fecha):
    try:
        fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
        nombre_dia_semana = fecha_objeto.strftime("%A")
        return nombre_dia_semana
    except ValueError:
        raise ValueError("Formato de fecha inválido. Por favor, ingrese la fecha en formato dd/mm/aaaa.")

def dia_siguiente(fecha):
    fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
    fecha_siguiente = fecha_objeto + timedelta(days=1)
    return fecha_siguiente.strftime("%d/%m/%Y"), fecha_siguiente.strftime("%A")

def main():
    print("\nEste programa te permite conocer el día de la semana para una fecha dada.\n")

    fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")

    try:
        dia = dia_semana(fecha)
        print(">>> El día de la semana para la fecha", fecha, "es:", dia)

        opcion = input("¿Quieres conocer el día siguiente? (S/N): ").upper()
        if opcion == "S":
            fecha_sig, dia_sig = dia_siguiente(fecha)
            print(">>> El día siguiente es:", dia_sig, "(", fecha_sig, ")")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

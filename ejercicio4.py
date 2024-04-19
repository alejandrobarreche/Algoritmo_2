class Alumno:
    def __init__(self, notas):
        self.notas = notas
        self.media = sum(notas) / len(notas)
        self.evaluacion = self.calcular_evaluacion()

    def calcular_evaluacion(self):
        if self.media > 15:
            return "Alumno con talento"
        elif 12 <= self.media <= 15:
            return "Con capacidad"
        else:
            return "Debe reorientarse"

def main():
    print("Este programa calcula la media y la evaluación de un alumno basándose en sus cuatro notas.")
    print("Las notas tendrán un valor entre 0 y 20")

    try:
        # Solicitar las cuatro notas al usuario
        notas_alumno = []
        for i in range(4):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if nota < 0 or nota > 20:
                raise ValueError("Las notas deben estar entre 0 y 20.")
            notas_alumno.append(nota)

        # Crear un objeto Alumno con las notas ingresadas
        alumno = Alumno(notas_alumno)

        # Imprimir la media y la evaluación del alumno
        print(f"\nLa media del alumno es: {alumno.media}")
        print(f"Evaluación: {alumno.evaluacion}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

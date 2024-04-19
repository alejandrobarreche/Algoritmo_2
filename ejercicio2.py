def clasificar_numeros(a, b):
    # Calculamos la suma y el producto de los números dados
    suma = a + b
    producto = a * b
    
    # Ordenamos los números de menor a mayor
    numeros_ordenados = sorted([a, b, suma, producto])

    # Creamos una lista de etiquetas para los valores
    etiquetas = ['a * b', 'a', 'a + b', 'b']

    # Creamos un diccionario para almacenar los resultados clasificados
    resultados_clasificados = {}

    # Asignamos los valores ordenados a sus etiquetas correspondientes
    for i in range(len(etiquetas)):
        resultados_clasificados[etiquetas[i]] = numeros_ordenados[i]

    return resultados_clasificados

def main():
    print("Este programa clasifica dos números y sus operaciones.")

    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        resultado = clasificar_numeros(a, b)

        print("Resultado de la clasificación:")
        for etiqueta, valor in resultado.items():
            print(f"{etiqueta}: {valor}")
    except ValueError:
        print("Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()

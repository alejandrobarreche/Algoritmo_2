# Ejercicios de La Alternativa ALGORITMOS
## Alejandro Barreche

## Algoritmo para Determinar el Día de la Semana y su Sucesor

Este algoritmo permite al usuario conocer el día de la semana para una fecha dada en formato "dd/mm/aaaa" y obtener el día siguiente a esa fecha.

### Función `dia_semana`

1. **Entrada de Datos**: 
   - El usuario ingresa una fecha en formato "dd/mm/aaaa".

2. **Procesamiento de la Fecha**: 
   - La fecha ingresada se convierte en un objeto de fecha y hora.

3. **Obtención del Día de la Semana**: 
   - Se extrae el nombre del día de la semana correspondiente a esa fecha.

### Función `dia_siguiente`

1. **Entrada de Datos**: 
   - Se recibe una fecha en formato "dd/mm/aaaa".

2. **Cálculo del Día Siguiente**: 
   - Se suma un día a la fecha dada.

3. **Formato de Salida**: 
   - Se devuelve la fecha del día siguiente junto con su nombre de día de la semana.


## Algoritmo para Clasificar Números y sus Operaciones

Este algoritmo clasifica dos números dados respecto a su suma y su producto, mostrando los valores en orden de menor a mayor.

### Función `clasificar_numeros`

1. **Cálculo de la Suma y el Producto**:
   - Se calculan la suma y el producto de los números dados.

2. **Ordenamiento de los Números**:
   - Se ordenan los números (a, b, suma, producto) de menor a mayor.

3. **Creación de Etiquetas**:
   - Se crea una lista de etiquetas para los valores ordenados: 'a * b', 'a', 'a + b', 'b'.

4. **Asignación de Resultados**:
   - Se crea un diccionario para almacenar los resultados clasificados.
   - Se asignan los valores ordenados a sus etiquetas correspondientes.


## Algoritmo para Calcular el Descuento en una Compra

Este algoritmo calcula el descuento aplicable a una compra según las siguientes condiciones:
- Se aplica un descuento del 5% en las compras con un importe entre 100€ y 500€.
- Se aplica un descuento del 8% en las compras con un importe superior a 500€.

### Función `calcular_descuento`

1. **Verificación del Importe**:
   - Se comprueba si el importe de la compra es válido (mayor que cero).
   - Si el importe es menor o igual a cero, se lanza un error.
   - Si el importe está entre 0 y 100€, el descuento es 0.

2. **Cálculo del Descuento**:
   - Si el importe está entre 100€ y 500€, se aplica un descuento del 5%.
   - Si el importe es superior a 500€, se aplica un descuento del 8%.

3. **Salida del Descuento**:
   - Se devuelve el importe del descuento calculado.



## Algoritmo para Calcular la Media y la Evaluación de un Alumno

Este algoritmo toma como entrada las cuatro notas de un alumno y calcula la media de las notas y la evaluación correspondiente, según los siguientes criterios:
- "Alumno con talento" si la media es superior a 15.
- "Con capacidad" si la media está comprendida entre 12 y 15.
- "Debe reorientarse" si la media es inferior a 12.

### Clase `Alumno`

1. **Inicialización**:
   - Se inicializa la clase `Alumno` con las notas obtenidas por el alumno.

2. **Cálculo de la Media**:
   - Se calcula la media de las cuatro notas.

3. **Cálculo de la Evaluación**:
   - Se determina la evaluación del alumno según su media.


## Algoritmo para Calcular el Descuento en el Parque Warner Madrid

Este algoritmo calcula el descuento al que tendrá derecho una familia que visita el Parque Warner Madrid, basado en la cantidad de niños que hay en la familia.

### Función `calcular_descuento`

1. **Verificación del Número de Niños**:
   - Se verifica si el número de niños en la familia es menor a 2. En ese caso, el descuento es 0.
   - Si hay 2 niños, se aplica un descuento del 10%.
   - Si hay 3 niños, se aplica un descuento del 15%.
   - Si hay 4 niños, se aplica un descuento del 18%.
   - Si hay 5 o más niños, se aplica un descuento del 18% más un 1% adicional por cada niño por encima de 4.

2. **Cálculo del Descuento**:
   - Se calcula el importe del descuento basado en la cantidad de niños en la familia.
  

## Algoritmo para Calcular el Descuento en la Compra de Microprocesadores

Este algoritmo calcula el descuento concedido por la empresa UNTEL para la compra al por mayor de microprocesadores, basado en la cantidad de componentes pedidos y el cliente que realiza el pedido.

### Función `calcular_descuento`

1. **Cálculo del Descuento por Cantidad de Componentes**:
   - Si la cantidad de componentes pedidos está entre 10,000 y 20,000, se aplica un descuento del 10%.
   - Si la cantidad está entre 20,001 y 40,000, se aplica un descuento del 15%.
   - Si la cantidad es mayor a 40,000, se aplica un descuento del 20%.
   - Si la cantidad es menor a 10,000, no se aplica ningún descuento.

2. **Ajuste del Descuento por Cliente**:
   - Si el cliente es "COMMAQ", se reduce el descuento en un 2%.
   - Si el cliente es "BEL", se aumenta el descuento en un 1%.


## Algoritmo para Calcular el Coste de un Viaje Escolar

Este algoritmo calcula el coste por alumno y el coste total de un viaje escolar, teniendo en cuenta la cantidad de alumnos participantes.

### Función `calcular_coste_viaje`

1. **Cálculo del Coste del Trayecto**:
   - Si la cantidad de alumnos es igual o inferior a 25, el coste del trayecto es de 67,30 € por alumno.
   - Si hay más de 25 alumnos, el coste del trayecto es de 61,00 € por alumno.

2. **Cálculo del Coste de la Comida**:
   - El coste de la comida es de 3,50 € por día y por alumno.

3. **Cálculo del Coste del Alojamiento**:
   - Si la cantidad de alumnos es inferior a 30, el coste del alojamiento es de 4,75 € por día y por alumno.
   - Para 30 a 35 alumnos, el coste es de 4,00 € por alumno.
   - Para más de 35 alumnos, el coste es de 3,50 € por alumno.

4. **Cálculo del Coste Total y por Alumno**:
   - Se suma el coste del trayecto, la comida y el alojamiento para obtener el coste total.
   - Se divide el coste total entre la cantidad de alumnos para obtener el coste por alumno.


## Algoritmo para Calcular la Prima Anual de los Empleados Camioneros de La Campana

Este algoritmo calcula la prima anual que reciben los empleados camioneros de la empresa La Campana, considerando su historial de accidentes, distancia recorrida y antigüedad en la empresa.

### Función `calcular_prima_anual`

1. **Cálculo de la Responsabilidad por Accidentes**:
   - Si el conductor no ha tenido accidentes con una responsabilidad igual o superior al 20 %, recibe la prima anual completa.
   - Si la responsabilidad supera el 20 %, se reduce la prima según el número de accidentes.

2. **Cálculo de la Prima de Distancia**:
   - La prima aumenta en un céntimo por kilómetro recorrido durante el año, con un máximo de 400 €.

3. **Cálculo de la Prima de Antigüedad**:
   - Se paga una prima de 200 € una vez transcurridos cuatro años de antigüedad.
   - Luego, aumenta 20,00 € por cada año adicional.

4. **Cálculo de la Prima Anual Total**:
   - Se suma la prima de distancia y la prima de antigüedad para obtener la prima anual total.




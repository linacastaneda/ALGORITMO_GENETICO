# Punto 1. Formulación del problema

## a) Variable de decisión

$$
x_i \in \{0,1\}, \quad i = 1,\dots,10
$$

Cada proyecto se modela mediante una variable binaria \(x_i\). Esta variable corresponde a un gen del cromosoma: toma el valor 1 cuando el proyecto \(P_i\) es seleccionado y 0 cuando es descartado.

De esta forma, dado que existen 10 proyectos, un individuo del algoritmo genético queda compuesto por diez genes binarios.

---

## b) Función objetivo

La función objetivo busca maximizar el beneficio total generado por los proyectos seleccionados. Para ello, se suma el beneficio \(b_i\) de cada proyecto multiplicado por su variable de decisión \(x_i\). De esta forma, únicamente aportan al beneficio total los proyectos cuyo gen tenga valor 1.

$$
\max B(X)=\sum_{i=1}^{10} b_i x_i
$$

donde \(b_i\) corresponde al beneficio del proyecto \(P_i\).

---

## c) Restricción principal

La restricción principal establece que el costo total de los proyectos seleccionados no puede superar el presupuesto máximo disponible de 50 unidades monetarias.

Para calcular este costo, se suma el costo \(c_i\) de cada proyecto multiplicado por su variable de decisión \(x_i\).

$$
C(X)=\sum_{i=1}^{10} c_i x_i \leq 50
$$

donde \(c_i\) corresponde al costo del proyecto \(P_i\).

Por lo tanto, una solución cuyo costo total sea superior a 50 unidades monetarias no cumple con la restricción del problema.

---

## d) Representación de un individuo

Un individuo se representa mediante un cromosoma binario de 10 genes, donde cada posición corresponde a uno de los 10 proyectos disponibles.

El valor 1 indica que el proyecto asociado a esa posición es seleccionado, mientras que el valor 0 indica que no es incluido en la solución.

Por ejemplo:

$$
X=(1,0,1,0,0,1,0,1,0,0)
$$

En este caso, el individuo selecciona los proyectos P1, P3, P6 y P8.

---

## e) Número de soluciones posibles

El espacio de búsqueda está compuesto por todas las combinaciones posibles de selección y no selección de los 10 proyectos.

Como cada gen puede tomar dos valores posibles, 0 o 1, el número total de soluciones diferentes es:

$$
2^{10}=1024
$$

Por lo tanto, existen 1024 soluciones posibles dentro del espacio de búsqueda.

## Cálculo manual del individuo propuesto

El individuo dado es:

$$
X=(1,0,1,1,0,0,1,0,1,0)
$$

Los proyectos seleccionados corresponden a P1, P3, P4, P7 y P9.

### Costo total

$$
C(X)=12+11+8+6+5=42
$$

### Beneficio total

$$
B(X)=24+23+15+11+9=82
$$

### Validación

Como:

$$
42 \leq 50
$$

el individuo cumple con la restricción presupuestal y representa una solución válida.

Por lo tanto:

- Costo total: 42
- Beneficio total: 82
- Solución válida: Sí
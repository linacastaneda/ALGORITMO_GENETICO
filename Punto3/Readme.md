
# Punto 3 - Operadores Genéticos

## Introducción

En este punto se implementan los principales operadores genéticos utilizados en el algoritmo genético para resolver el problema de selección óptima de proyectos.

El problema consiste en seleccionar proyectos de innovación buscando maximizar el beneficio total, sin superar un presupuesto máximo de **50 unidades**.

Cada proyecto está representado mediante un cromosoma binario de 10 posiciones, donde:

* `1` significa que el proyecto es seleccionado.
* `0` significa que el proyecto no es seleccionado.

Este punto utiliza la población y la función de aptitud desarrolladas anteriormente y agrega los operadores necesarios para generar nuevos individuos.

---

## Objetivo

Implementar y demostrar los siguientes operadores genéticos:

1. **Selección por torneo de tamaño 3.**
2. **Cruce de un punto.**
3. **Mutación binaria con probabilidad de 0.05.**

Además, se muestra paso a paso cómo estos operadores transforman los individuos seleccionados.

---

## Problema

Se tienen 10 proyectos:

| Proyecto | Costo | Beneficio |
| -------- | ----: | --------: |
| P1       |    12 |        24 |
| P2       |     7 |        13 |
| P3       |    11 |        23 |
| P4       |     8 |        15 |
| P5       |     9 |        16 |
| P6       |    14 |        28 |
| P7       |     6 |        11 |
| P8       |    10 |        19 |
| P9       |     5 |         9 |
| P10      |    13 |        25 |

El presupuesto máximo disponible es:

**50**

La aptitud utilizada corresponde a la función definida en el Punto 2, con:

```text
lambda = 5
```

---

# Representación del individuo

Cada individuo se representa mediante un cromosoma binario de 10 genes.

Por ejemplo:

```text
0111001011
```

Representa:

```text
P1  P2  P3  P4  P5  P6  P7  P8  P9  P10
 0   1   1   1   0   0   1   0   1    1
```

Por lo tanto, los proyectos seleccionados son:

```text
P2, P3, P4, P7, P9 y P10
```

---

# 1. Selección por torneo

La selección se realiza mediante un torneo de tamaño **3**.

El procedimiento es:

1. Se seleccionan aleatoriamente tres individuos de la población.
2. Se calcula o consulta la aptitud de cada uno.
3. Se comparan sus aptitudes.
4. El individuo con mayor aptitud es seleccionado como padre.

Por ejemplo:

```text
Candidato 1 → Aptitud = 73
Candidato 2 → Aptitud = 96
Candidato 3 → Aptitud = 68
```

El ganador sería:

```text
Candidato 2
```

porque tiene la mayor aptitud.

La función utilizada es:

```python
def seleccionar_padre(poblacion, tam_torneo=3):
```

---

# 2. Cruce de un punto

Después de seleccionar dos padres, se realiza un cruce de un punto.

Primero se selecciona aleatoriamente una posición de corte dentro del cromosoma.

Por ejemplo:

```text
Padre 1: 1011 | 101010
Padre 2: 0111 | 001011
```

Después del cruce se intercambian las partes posteriores:

```text
Hijo 1: 1011 | 001011
Hijo 2: 0111 | 101010
```

De esta manera, los hijos reciben información genética de ambos padres.

La función utilizada es:

```python
def cruzar(padre1, padre2):
```

---

# 3. Mutación binaria

La mutación permite introducir diversidad en la población.

En este ejercicio se utiliza una probabilidad de mutación de:

```text
pm = 0.05
```

Cada gen se revisa individualmente.

Si ocurre una mutación, el valor del gen cambia:

```text
0 → 1
1 → 0
```

Por ejemplo:

```text
Antes:
1011001010

Después:
1010001010
```

En este caso, uno de los genes cambió de `1` a `0`.

La función utilizada es:

```python
def mutar(cromosoma, pm=PROB_MUTACION):
```

---

# Flujo del Punto 3

Los operadores se aplican siguiendo este proceso:

```text
             POBLACIÓN
                 │
                 ▼
        SELECCIÓN POR TORNEO
            (3 individuos)
                 │
                 ▼
             PADRE 1
             PADRE 2
                 │
                 ▼
        CRUCE DE UN PUNTO
                 │
                 ▼
        HIJO 1       HIJO 2
                 │
                 ▼
             MUTACIÓN
             pm = 0.05
                 │
                 ▼
       HIJO 1 FINAL
       HIJO 2 FINAL
```

---

# Funciones implementadas

El archivo `punto3_operadores_geneticos.py` contiene las siguientes funciones principales:

| Función                | Descripción                                    |
| ---------------------- | ---------------------------------------------- |
| `generar_individuo()`  | Genera un cromosoma binario.                   |
| `generar_poblacion()`  | Genera la población inicial.                   |
| `calcular_costo()`     | Calcula el costo de un individuo.              |
| `calcular_beneficio()` | Calcula el beneficio de un individuo.          |
| `calcular_aptitud()`   | Calcula la aptitud utilizando la penalización. |
| `es_valida()`          | Comprueba si se respeta el presupuesto.        |
| `seleccionar_padre()`  | Realiza selección por torneo.                  |
| `cruzar()`             | Realiza cruce de un punto.                     |
| `mutar()`              | Realiza mutación binaria.                      |

---

# Demostración

El programa genera una población de **20 individuos** y posteriormente demuestra:

### Selección

Muestra los tres candidatos que participan en cada torneo y determina cuál tiene la mayor aptitud.

### Cruce

Muestra:

* Padre 1.
* Padre 2.
* Punto de cruce.
* Hijo 1 antes de la mutación.
* Hijo 2 antes de la mutación.

### Mutación

Muestra:

* Cromosoma antes de mutar.
* Posiciones que fueron mutadas.
* Cromosoma después de mutar.

Finalmente, muestra la información de los hijos obtenidos:

* Cromosoma.
* Proyectos seleccionados.
* Costo.
* Beneficio.
* Aptitud.
* Validez.

---

# Parámetros utilizados

| Parámetro                |    Valor |
| ------------------------ | -------: |
| Número de proyectos      |       10 |
| Tamaño de población      |       20 |
| Presupuesto              |       50 |
| Lambda                   |        5 |
| Tamaño del torneo        |        3 |
| Probabilidad de mutación |     0.05 |
| Tipo de cruce            | Un punto |
| Tipo de mutación         |  Binaria |

---

# Archivo principal

El código de este punto se encuentra en:

```text
punto3_operadores_geneticos.py
```

Para ejecutarlo desde la terminal:

```bash
python punto3_operadores_geneticos.py
```

---

# Conclusión

En este punto se implementaron los operadores fundamentales que permiten modificar y seleccionar individuos dentro de una población genética.

La **selección por torneo** permite elegir padres favoreciendo individuos con mayor aptitud. El **cruce de un punto** combina la información genética de dos padres para producir nuevos individuos. Finalmente, la **mutación binaria** introduce pequeños cambios aleatorios en los cromosomas para mantener diversidad en la población.

Estos operadores constituyen la base para la generación de nuevas soluciones dentro de un algoritmo genético.

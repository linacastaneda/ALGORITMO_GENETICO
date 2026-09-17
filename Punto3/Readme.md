
# Punto 3 - Operadores Genéticos

## Introducción

En este punto se implementan los principales operadores genéticos utilizados en un algoritmo genético para resolver el problema de selección óptima de proyectos.

El problema consiste en seleccionar proyectos de innovación buscando **maximizar el beneficio total**, sin superar un presupuesto máximo de **50 unidades**.

Cada proyecto se representa mediante un cromosoma binario de 10 posiciones:

* `1` → el proyecto es seleccionado.
* `0` → el proyecto no es seleccionado.

Este punto toma como base la representación y la función de aptitud desarrolladas en el **Punto 2** y agrega los operadores necesarios para generar nuevos individuos.

---

# Objetivo

Implementar y demostrar los siguientes operadores genéticos:

1. **Selección por torneo de tamaño 3.**
2. **Cruce de un punto.**
3. **Mutación binaria con probabilidad de 0.05.**

Además, el programa permite observar paso a paso cómo estos operadores trabajan sobre los individuos de la población.

---

# Problema

Se tienen 10 proyectos de innovación:

| Proyecto | Costo | Beneficio |
| :------: | ----: | --------: |
|    P1    |    12 |        24 |
|    P2    |     7 |        13 |
|    P3    |    11 |        23 |
|    P4    |     8 |        15 |
|    P5    |     9 |        16 |
|    P6    |    14 |        28 |
|    P7    |     6 |        11 |
|    P8    |    10 |        19 |
|    P9    |     5 |         9 |
|    P10   |    13 |        25 |

El presupuesto máximo disponible es:

**50**

La función de aptitud utilizada corresponde a la definida en el Punto 2, utilizando:

```text
lambda = 5
```

Cuando una solución no supera el presupuesto, su aptitud corresponde a su beneficio.

Cuando supera el presupuesto, se aplica una penalización de acuerdo con el exceso:

```text
Aptitud = Beneficio - lambda × Exceso
```

---

# Representación del individuo

Cada individuo está representado mediante un cromosoma binario de 10 genes.

Por ejemplo:

```text
0111001011
```

Cada posición corresponde a un proyecto:

```text
P1  P2  P3  P4  P5  P6  P7  P8  P9  P10
 0   1   1   1   0   0   1   0   1    1
```

Por lo tanto, los proyectos seleccionados serían:

```text
P2, P3, P4, P7, P9, P10
```

---

# 1. Selección por torneo

## ¿Qué es?

La selección por torneo permite elegir los padres que participarán en el proceso de reproducción.

En este ejercicio se utiliza un **torneo de tamaño 3**.

El procedimiento es:

1. Se seleccionan aleatoriamente tres individuos de la población.
2. Se obtiene la aptitud de cada individuo.
3. Se comparan sus aptitudes.
4. El individuo con mayor aptitud gana el torneo.
5. El ganador es seleccionado como padre.

### Ejemplo

Supongamos que se obtiene el siguiente torneo:

```text
Candidato 1 → Aptitud = 73
Candidato 2 → Aptitud = 96
Candidato 3 → Aptitud = 68
```

El ganador sería:

```text
Candidato 2
```

porque presenta la mayor aptitud.

La función implementada es:

```python
def seleccionar_padre(poblacion, tam_torneo=3):
```

---

# 2. Cruce de un punto

## ¿Qué es?

El cruce combina la información genética de dos padres para generar nuevos individuos.

Primero se selecciona aleatoriamente un punto de corte dentro del cromosoma.

Por ejemplo:

```text
Padre 1: 1011 | 101010
Padre 2: 0111 | 001011
```

Se intercambian las partes que se encuentran después del punto de corte:

```text
Hijo 1: 1011 | 001011
Hijo 2: 0111 | 101010
```

De esta manera, cada hijo contiene información genética de ambos padres.

La función implementada es:

```python
def cruzar(padre1, padre2):
```

El punto de cruce se selecciona aleatoriamente entre las posiciones válidas del cromosoma.

---

# 3. Mutación binaria

## ¿Qué es?

La mutación introduce pequeños cambios aleatorios en los cromosomas.

En este ejercicio se utiliza una probabilidad de mutación de:

```text
pm = 0.05
```

Esto corresponde a una probabilidad del **5 % para cada gen**.

Cuando un gen muta, cambia su valor:

```text
0 → 1
1 → 0
```

### Ejemplo

Antes de la mutación:

```text
1011001010
```

Después de una posible mutación:

```text
1010001010
```

En este ejemplo, uno de los genes cambió de `1` a `0`.

La función implementada es:

```python
def mutar(cromosoma, pm=PROB_MUTACION):
```

La mutación se realiza de forma independiente para cada gen.

Por esta razón, una ejecución puede presentar una o varias mutaciones, pero también es posible que no ocurra ninguna.

---

# Flujo de los operadores genéticos

El proceso implementado en este punto puede representarse de la siguiente manera:

```text
                    POBLACIÓN
                        │
                        ▼
              SELECCIÓN POR TORNEO
                    Tamaño = 3
                        │
                 ┌──────┴──────┐
                 ▼             ▼
              PADRE 1       PADRE 2
                 │             │
                 └──────┬──────┘
                        ▼
                CRUCE DE UN PUNTO
                        │
                 ┌──────┴──────┐
                 ▼             ▼
               HIJO 1        HIJO 2
                 │             │
                 └──────┬──────┘
                        ▼
                     MUTACIÓN
                    pm = 0.05
                        │
                 ┌──────┴──────┐
                 ▼             ▼
           HIJO 1 FINAL   HIJO 2 FINAL
```

---

# Funciones implementadas

El archivo `punto3_operadores_geneticos.py` contiene las funciones necesarias para realizar el proceso.

| Función                     | Descripción                                       |
| --------------------------- | ------------------------------------------------- |
| `generar_individuo()`       | Genera un cromosoma binario.                      |
| `generar_poblacion()`       | Genera la población inicial.                      |
| `calcular_costo()`          | Calcula el costo de un individuo.                 |
| `calcular_beneficio()`      | Calcula el beneficio de un individuo.             |
| `calcular_aptitud()`        | Calcula la aptitud utilizando la penalización.    |
| `es_valida()`               | Comprueba si el individuo respeta el presupuesto. |
| `proyectos_seleccionados()` | Identifica los proyectos seleccionados.           |
| `seleccionar_padre()`       | Realiza la selección mediante torneo.             |
| `cruzar()`                  | Realiza el cruce de un punto.                     |
| `mutar()`                   | Realiza la mutación binaria.                      |

---

# Parámetros utilizados

| Parámetro                |    Valor |
| ------------------------ | -------: |
| Número de proyectos      |       10 |
| Tamaño de población      |       20 |
| Presupuesto máximo       |       50 |
| Lambda                   |        5 |
| Tamaño del torneo        |        3 |
| Probabilidad de mutación |     0.05 |
| Tipo de cruce            | Un punto |
| Tipo de mutación         |  Binaria |

---

# Demostración del Punto 3

El programa realiza una demostración completa de los operadores genéticos.

## Selección

Se muestran los tres individuos que participan en cada torneo junto con su respectiva aptitud.

Posteriormente se identifica el individuo ganador, que será utilizado como padre.

Se realiza el proceso para obtener dos padres.

## Cruce

Después de obtener los dos padres, el programa muestra:

* Padre 1.
* Padre 2.
* Punto de cruce.
* Hijo 1 antes de la mutación.
* Hijo 2 antes de la mutación.

## Mutación

Posteriormente se aplica la probabilidad de mutación `0.05` a cada gen.

El programa muestra:

* Cromosoma antes de mutar.
* Posiciones que fueron mutadas.
* Cromosoma después de mutar.

Finalmente se presenta la información de los hijos obtenidos.

---

# Información de los hijos finales

Para cada hijo final se muestra:

* Cromosoma.
* Proyectos seleccionados.
* Costo.
* Beneficio.
* Aptitud.
* Validez respecto al presupuesto.

Esto permite comprobar el efecto de los operadores sobre las soluciones.

---

# Relación con el Punto 2

El Punto 3 utiliza como base los elementos desarrollados anteriormente en el Punto 2.

Se mantienen:

* Los 10 proyectos.
* Los costos.
* Los beneficios.
* El presupuesto máximo de 50.
* La representación binaria.
* El cálculo del costo.
* El cálculo del beneficio.
* La función de aptitud.
* La penalización con `lambda = 5`.

A partir de estos elementos se incorporan los operadores genéticos:

```text
Punto 2
   │
   ├── Individuos
   ├── Población
   ├── Costo
   ├── Beneficio
   └── Aptitud
          │
          ▼
Punto 3
   │
   ├── Selección
   ├── Cruce
   └── Mutación
```

---

# Estructura del proyecto

La carpeta correspondiente a este punto está organizada de la siguiente manera:

```text
Punto3/
│
├── punto3_operadores_geneticos.py
│
└── README.md
```

### `punto3_operadores_geneticos.py`

Contiene la implementación de los operadores genéticos y la demostración del proceso.

### `README.md`

Contiene la explicación del problema, los operadores utilizados, los parámetros y la forma de ejecución.

---

# Requisitos

Para ejecutar el programa se necesita:

* Python 3.x
* Visual Studio Code u otro editor de código.
* Terminal para ejecutar el archivo.

No se utilizan bibliotecas externas para implementar los operadores genéticos.

El programa utiliza la biblioteca estándar `random` de Python.

---

# Ejecución

Desde la terminal, ubicándose dentro de la carpeta `Punto3`, ejecutar:

```bash
python punto3_operadores_geneticos.py
```

En algunos sistemas también puede utilizarse:

```bash
py punto3_operadores_geneticos.py
```

También es posible ejecutar el programa directamente desde Visual Studio Code utilizando la opción **Run Python File**.

---

# Resultados

Al ejecutar el programa se muestran los resultados correspondientes a:

1. Población inicial.
2. Candidatos de cada torneo.
3. Padres seleccionados.
4. Punto de cruce.
5. Hijos antes de la mutación.
6. Genes que fueron mutados.
7. Hijos después de la mutación.
8. Costo de los hijos.
9. Beneficio de los hijos.
10. Aptitud de los hijos.
11. Validez de los hijos.

Los resultados numéricos de la ejecución se obtienen directamente al ejecutar el programa.

---

# Conclusión

En este punto se implementaron los tres operadores genéticos solicitados: **selección por torneo, cruce de un punto y mutación binaria**.

La selección por torneo permite escoger padres utilizando la aptitud de los individuos. El cruce de un punto combina la información genética de dos padres para producir nuevos individuos. Finalmente, la mutación binaria permite introducir cambios aleatorios en los genes y mantener diversidad dentro de las soluciones.

Estos operadores permiten transformar la población inicial y generar nuevos individuos, constituyendo los mecanismos fundamentales de reproducción de un algoritmo genético.

---

## Autor

**Taller de Introducción a la Inteligencia Artificial**

**Punto 3 - Operadores Genéticos**

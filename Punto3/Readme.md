# Punto 3 - Operadores Genéticos

## Introducción

En este punto se implementan los principales operadores genéticos utilizados en un algoritmo genético para resolver el problema de selección óptima de proyectos.

El problema consiste en seleccionar proyectos de innovación buscando **maximizar el beneficio total**, sin superar un presupuesto máximo de **50 unidades**.

Cada proyecto se representa mediante un cromosoma binario de 10 posiciones:

- `1` → el proyecto es seleccionado.
- `0` → el proyecto no es seleccionado.

Este punto toma como base la representación de los individuos y la función de aptitud desarrolladas en el **Punto 2**, y agrega los operadores necesarios para generar nuevos individuos.

---

# Objetivo

Implementar y demostrar los siguientes operadores genéticos:

1. **Selección por torneo de tamaño 3.**
2. **Cruce de un punto.**
3. **Mutación binaria con probabilidad de 0.05.**

Además, el programa permite observar paso a paso cómo estos operadores trabajan sobre los individuos de la población.

---

# Problema

Se tienen 10 proyectos de innovación. Cada proyecto tiene asociado un costo y un beneficio.

El objetivo general es seleccionar proyectos buscando maximizar el beneficio sin superar un presupuesto máximo de 50 unidades.

### Datos de los proyectos

| Proyecto | Costo | Beneficio |
| :------: | ----: | --------: |
| P1 | 12 | 24 |
| P2 | 7 | 13 |
| P3 | 11 | 23 |
| P4 | 8 | 15 |
| P5 | 9 | 16 |
| P6 | 14 | 28 |
| P7 | 6 | 11 |
| P8 | 10 | 19 |
| P9 | 5 | 9 |
| P10 | 13 | 25 |

### Presupuesto máximo

```text
50
```

---

# Función de aptitud

La función de aptitud utilizada corresponde a la definida en el Punto 2.

Para las soluciones cuyo costo no supera el presupuesto:

```text
Aptitud = Beneficio
```

Cuando el costo supera el presupuesto, se aplica una penalización.

El valor utilizado es:

```text
lambda = 5
```

La función completa es:

```text
Si costo <= 50:

    Aptitud = Beneficio

Si costo > 50:

    Aptitud = Beneficio - lambda × (costo - 50)
```

De esta manera, las soluciones que superan el presupuesto reciben una penalización proporcional al exceso.

---

# Representación del individuo

Cada individuo se representa mediante un cromosoma binario de 10 genes.

Por ejemplo:

```text
0111001011
```

Cada posición corresponde a un proyecto:

```text
P1  P2  P3  P4  P5  P6  P7  P8  P9  P10
 0   1   1   1   0   0   1   0   1    1
```

Por lo tanto, los proyectos seleccionados son:

```text
P2, P3, P4, P7, P9, P10
```

El costo correspondiente es:

```text
7 + 11 + 8 + 6 + 5 + 13 = 50
```

Y el beneficio:

```text
13 + 23 + 15 + 11 + 9 + 25 = 96
```

Como el costo es exactamente igual al presupuesto, el individuo es válido y su aptitud es:

```text
Aptitud = 96
```

---

# 1. Selección por torneo

## ¿Qué es?

La selección por torneo permite escoger los individuos que participarán como padres en el proceso de reproducción.

En este ejercicio se utiliza un **torneo de tamaño 3**.

El procedimiento es:

1. Se seleccionan aleatoriamente tres individuos de la población.
2. Se obtiene la aptitud de cada individuo.
3. Se comparan las aptitudes.
4. El individuo con mayor aptitud gana el torneo.
5. El ganador es seleccionado como padre.

La función implementada es:

```python
def seleccionar_padre(poblacion, tam_torneo=3):
```

### Ejemplo

Si los participantes de un torneo presentan:

| Candidato | Aptitud |
| :--------: | ------: |
| 1 | 73 |
| 2 | 96 |
| 3 | 68 |

El candidato 2 gana el torneo porque tiene la mayor aptitud.

Para generar los dos padres necesarios para el cruce, el proceso de selección se realiza dos veces.

---

# 2. Cruce de un punto

## ¿Qué es?

El cruce permite combinar la información genética de dos padres para generar nuevos individuos.

Primero se selecciona aleatoriamente un punto de cruce dentro del cromosoma.

Después, se intercambian las partes posteriores de los dos padres.

Por ejemplo:

```text
Padre 1 = 1011 | 101010
Padre 2 = 0111 | 001011
```

Después del cruce:

```text
Hijo 1 = 1011 | 001011
Hijo 2 = 0111 | 101010
```

De esta forma, cada hijo contiene información genética proveniente de ambos padres.

La función implementada es:

```python
def cruzar(padre1, padre2):
```

El punto de cruce se selecciona aleatoriamente entre las posiciones válidas del cromosoma.

---

# 3. Mutación binaria

## ¿Qué es?

La mutación introduce cambios aleatorios en los cromosomas.

Para este ejercicio se utiliza una probabilidad de mutación de:

```text
pm = 0.05
```

Esto corresponde a una probabilidad del **5 % para cada gen**.

Cuando un gen es seleccionado para mutar, su valor cambia:

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
def mutar(cromosoma, pm=0.05):
```

La mutación se realiza de manera independiente para cada gen.

Por esta razón, una ejecución puede presentar una o varias mutaciones, pero también puede ocurrir que no se produzca ninguna.

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

# Demostración del Punto 3

El programa realiza una demostración completa de los operadores solicitados utilizando una población inicial de 20 individuos.

El proceso realizado es:

1. Generar la población inicial.
2. Realizar un torneo de 3 individuos para seleccionar el Padre 1.
3. Realizar un segundo torneo de 3 individuos para seleccionar el Padre 2.
4. Realizar el cruce de un punto.
5. Mostrar los hijos antes de la mutación.
6. Aplicar la mutación binaria con `pm = 0.05`.
7. Mostrar los hijos después de la mutación.
8. Calcular el costo, beneficio y aptitud de los hijos finales.
9. Comprobar si los hijos respetan el presupuesto.

---

# Ejemplo manual solicitado

La ejecución utilizada para demostrar el Punto 3 produjo los siguientes resultados.

## Selección del Padre 1

Primer torneo:

| Candidato | Cromosoma | Aptitud |
| :--------: | :-------- | ------: |
| 1 | 0000001011 | 45.00 |
| 2 | 0110001111 | 90.00 |
| 3 | 0010000010 | 32.00 |

El ganador fue:

```text
PADRE 1 = 0110001111
```

Información del Padre 1:

| Característica | Resultado |
|----------------|-----------|
| Cromosoma | 0110001111 |
| Proyectos | P2, P3, P7, P8, P9, P10 |
| Costo | 52 |
| Beneficio | 100 |
| Aptitud | 90.00 |
| Válida | No |

Como el costo es 52, supera el presupuesto en 2 unidades.

La aptitud se calcula:

```text
100 - 5 × (52 - 50)

100 - 10 = 90
```

---

# Selección del Padre 2

Segundo torneo:

| Candidato | Cromosoma | Aptitud |
| :--------: | :-------- | ------: |
| 1 | 0011100100 | 73.00 |
| 2 | 0111001011 | 96.00 |
| 3 | 1111011010 | 58.00 |

El ganador fue:

```text
PADRE 2 = 0111001011
```

Información del Padre 2:

| Característica | Resultado |
|----------------|-----------|
| Cromosoma | 0111001011 |
| Proyectos | P2, P3, P4, P7, P9, P10 |
| Costo | 50 |
| Beneficio | 96 |
| Aptitud | 96.00 |
| Válida | Sí |

---

# Cruce de un punto

Los padres seleccionados fueron:

```text
PADRE 1 = 0110001111
PADRE 2 = 0111001011
```

El punto de cruce seleccionado por el programa fue:

```text
7
```

Los cromosomas se pueden representar como:

```text
PADRE 1 = 0110001 | 111
PADRE 2 = 0111001 | 011
```

Después de intercambiar las partes posteriores:

```text
HIJO 1 = 0110001 | 011
HIJO 2 = 0111001 | 111
```

Por lo tanto, los hijos antes de la mutación fueron:

```text
HIJO 1 = 0110001011
HIJO 2 = 0111001111
```

---

# Mutación

La probabilidad de mutación utilizada fue:

```text
pm = 0.05
```

Durante esta ejecución no se produjo ninguna mutación.

Por lo tanto:

| Hijo | Antes | Mutaciones | Después |
|------|-------|------------|---------|
| Hijo 1 | 0110001011 | Ninguna | 0110001011 |
| Hijo 2 | 0111001111 | Ninguna | 0111001111 |

El hecho de que no haya ocurrido una mutación en esta ejecución es posible debido al carácter aleatorio del proceso.

La función de mutación sí se ejecutó y revisó cada uno de los genes utilizando la probabilidad establecida del 5 %.

---

# Resultados finales

Los hijos obtenidos después del cruce y la mutación fueron:

| Hijo | Cromosoma | Proyectos | Costo | Beneficio | Aptitud | Válida |
|------|-----------|-----------|------:|----------:|--------:|:------:|
| Hijo 1 | 0110001011 | P2, P3, P7, P9, P10 | 42 | 81 | 81.00 | Sí |
| Hijo 2 | 0111001111 | P2, P3, P4, P7, P8, P9, P10 | 60 | 115 | 65.00 | No |

## Hijo 1

Cromosoma:

```text
0110001011
```

Proyectos seleccionados:

```text
P2, P3, P7, P9, P10
```

Costo:

```text
7 + 11 + 6 + 5 + 13 = 42
```

Beneficio:

```text
13 + 23 + 11 + 9 + 25 = 81
```

Como el costo no supera el presupuesto:

```text
Aptitud = 81
```

---

## Hijo 2

Cromosoma:

```text
0111001111
```

Proyectos seleccionados:

```text
P2, P3, P4, P7, P8, P9, P10
```

Costo:

```text
7 + 11 + 8 + 6 + 10 + 5 + 13 = 60
```

Beneficio:

```text
13 + 23 + 15 + 11 + 19 + 9 + 25 = 115
```

Como el costo supera el presupuesto:

```text
Aptitud = 115 - 5 × (60 - 50)

Aptitud = 115 - 50

Aptitud = 65
```

Por lo tanto, aunque el beneficio del hijo es 115, su aptitud queda en 65 debido a la penalización por superar el presupuesto.

---

# Tabla resumen del proceso

La demostración completa puede resumirse de la siguiente manera:

| Etapa | Resultado |
|-------|-----------|
| Padre 1 | 0110001111 |
| Padre 2 | 0111001011 |
| Punto de cruce | 7 |
| Hijo 1 antes de mutación | 0110001011 |
| Hijo 2 antes de mutación | 0111001111 |
| Mutación Hijo 1 | Ninguna |
| Mutación Hijo 2 | Ninguna |
| Hijo 1 final | 0110001011 |
| Hijo 2 final | 0111001111 |

---

# Funciones implementadas

El archivo `punto3_operadores_geneticos.py` contiene las funciones utilizadas para realizar el proceso.

| Función | Descripción |
|---------|-------------|
| `generar_individuo()` | Genera un cromosoma binario de 10 genes. |
| `generar_poblacion()` | Genera la población inicial. |
| `calcular_costo()` | Calcula el costo total de un individuo. |
| `calcular_beneficio()` | Calcula el beneficio total de un individuo. |
| `calcular_aptitud()` | Calcula la aptitud aplicando la penalización correspondiente. |
| `es_valida()` | Comprueba si el individuo respeta el presupuesto. |
| `proyectos_seleccionados()` | Identifica los proyectos representados por los genes en 1. |
| `seleccionar_padre()` | Realiza la selección mediante torneo. |
| `cruzar()` | Realiza el cruce de un punto. |
| `mutar()` | Realiza la mutación binaria. |
| `mostrar_individuo()` | Muestra la información de un individuo. |
| `demostracion_punto3()` | Ejecuta la demostración completa del Punto 3. |

---

# Parámetros utilizados

| Parámetro | Valor |
|-----------|------:|
| Número de proyectos | 10 |
| Tamaño de población | 20 |
| Presupuesto máximo | 50 |
| Lambda de penalización | 5 |
| Tamaño del torneo | 3 |
| Probabilidad de mutación | 0.05 |
| Tipo de cruce | Un punto |
| Tipo de mutación | Binaria |

---

# Relación con el Punto 2

El Punto 3 utiliza como base los elementos desarrollados anteriormente en el Punto 2.

Se mantienen:

- Los 10 proyectos.
- Los costos.
- Los beneficios.
- El presupuesto máximo de 50.
- La representación binaria.
- El cálculo del costo.
- El cálculo del beneficio.
- La función de aptitud.
- La penalización con `lambda = 5`.

A partir de estos elementos se incorporan los operadores genéticos:

```text
PUNTO 2
   │
   ├── Individuos
   ├── Población
   ├── Costo
   ├── Beneficio
   └── Aptitud
          │
          ▼
PUNTO 3
   │
   ├── Selección por torneo
   ├── Cruce de un punto
   └── Mutación binaria
```

---

# Ejecución del programa

Para ejecutar el programa se debe ingresar a la carpeta `Punto3`.

En Windows PowerShell:

```powershell
cd Punto3
```

Luego ejecutar:

```powershell
python punto3_operadores_geneticos.py
```

También puede utilizarse:

```powershell
py punto3_operadores_geneticos.py
```

El programa mostrará en la consola:

1. La población inicial.
2. Los participantes del primer torneo.
3. El Padre 1 seleccionado.
4. Los participantes del segundo torneo.
5. El Padre 2 seleccionado.
6. El punto de cruce.
7. Los hijos antes de la mutación.
8. Las mutaciones realizadas.
9. Los hijos después de la mutación.
10. El costo, beneficio, aptitud y validez de los hijos finales.

---

# Estructura del proyecto

La estructura correspondiente al Punto 3 es:

```text
Punto3/
│
├── punto3_operadores_geneticos.py
│
└── README.md
```

### `punto3_operadores_geneticos.py`

Contiene la implementación en Python de los operadores genéticos y la demostración solicitada.

### `README.md`

Contiene la documentación del Punto 3, incluyendo:

- Descripción del problema.
- Representación del cromosoma.
- Función de aptitud.
- Selección por torneo.
- Cruce de un punto.
- Mutación binaria.
- Ejemplo manual.
- Tablas de resultados.
- Funciones implementadas.
- Parámetros utilizados.
- Instrucciones de ejecución.

---

# Requisitos

Para ejecutar el programa se necesita:

- Python 3.x.
- Visual Studio Code u otro editor de código.
- Terminal para ejecutar el archivo.

El programa utiliza la biblioteca estándar `random` de Python y no requiere instalar bibliotecas externas para los operadores genéticos.

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

Los resultados numéricos de la demostración documentada en este README corresponden a una ejecución del programa con la semilla aleatoria utilizada en el código.

---

# Conclusión

En este punto se implementaron y demostraron los tres operadores genéticos solicitados: **selección por torneo de tamaño 3, cruce de un punto y mutación binaria**.

La selección por torneo permite escoger los padres utilizando la aptitud de los individuos. Posteriormente, el cruce de un punto combina la información genética de los dos padres para generar nuevos individuos.

Finalmente, la mutación binaria revisa cada gen utilizando una probabilidad del 5 %, permitiendo introducir cambios aleatorios en los cromosomas.

En la ejecución presentada no se produjo ninguna mutación, por lo que los cromosomas finales fueron iguales a los obtenidos después del cruce.

El resultado permite observar de manera práctica cómo los operadores genéticos transforman los individuos de una población y generan nuevas posibles soluciones para el problema de selección de proyectos.

---

# Autor

**Taller de Introducción a la Inteligencia Artificial**

**Punto 3 - Operadores Genéticos**

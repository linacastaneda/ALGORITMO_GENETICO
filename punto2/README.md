# Punto 2 — Población inicial y función de aptitud

Este README pertenece a la carpeta del **punto 2** del taller. Responde las dudas del
punto y documenta sus archivos.

## Qué hace este punto

- Genera una población inicial aleatoria de cromosomas binarios (N = 20, configurable).
- Calcula costo, beneficio y aptitud de cada individuo.
- Penaliza las soluciones que exceden el presupuesto (≤ 50) mediante el parámetro **λ**.
- Muestra por individuo: cromosoma, proyectos seleccionados, costo total, beneficio total,
  aptitud y si la solución es válida.

## Archivos de esta carpeta

```
punto2/
├── punto2.py                       # Código: población inicial + función de aptitud (λ)
├── resultados_punto2.txt           # Salida de una ejecución (seed 42)
├── resultados_punto2_poblacion.csv # Datos: los 20 individuos de la población
├── resultados_punto2_lambda.csv    # Datos: sensibilidad de la aptitud frente a λ
├── ejercicios_punto2.md            # Desarrollo del punto 2 (ejercicio + análisis de λ)
└── README.md                       # Este archivo (dudas resueltas del punto)
```

## Ejecución

```bash
python -X utf8 "punto2/punto2.py"
```

Solo requiere Python estándar. El script regenera `resultados_punto2.txt` automáticamente.

---

## Dudas del punto 2 (respondidas)

### 1. ¿Qué significa λ (lambda)?

λ es un número que se elige y que **controla qué tan fuerte se castiga a las soluciones
que se pasan del presupuesto**. Es el "precio" que se le cobra por **cada unidad de exceso**
sobre el presupuesto:

```
fitness(X) = B(X)                           si C(X) ≤ 50
fitness(X) = B(X) − λ · (C(X) − 50)         si C(X) > 50
```

<img width="550" height="95" alt="image" src="https://github.com/user-attachments/assets/56db6f7a-d2f1-480a-8289-6ac1c810809c" />


Ejemplo con los datos reales de la ejecución:
- Un individuo inválido con beneficio **98** que gasta **51** (exceso = 1) → cromosoma `1011101010`.
- La mejor solución válida obtiene **96** (individuo `0111001011`).

Aptitud del inválido según λ (B(X) − λ·(C(X) − 50) = 98 − λ·1):

| λ | Aptitud del inválido | Comparación con la mejor válida (96.00) |
|---|---|---|
| 0 | 98.00 | igual a su beneficio (sin penalización) |
| 1 | 97.00 | **supera** → conviene violar el presupuesto |
| 2 | 96.00 | iguala |
| 3 | 95.00 | por debajo |
| **5** | **93.00** | por debajo → gastar de más "no conviene" |
| 10 | 88.00 | por debajo |
| 20 | 78.00 | por debajo |
| 50 | 48.00 | por debajo |

Tabla completa en [`resultados_punto2_lambda.csv`](resultados_punto2_lambda.csv).

### 2. ¿Qué pasa si λ es demasiado pequeño?

La penalización es débil. Una solución que excede el presupuesto puede quedar con
**mayor aptitud que la mejor solución válida**. El algoritmo genético tenderá a favorecer
(e incluso a converger a) soluciones **inválidas** que se pasan del presupuesto. Con λ = 1,
el inválido del ejemplo queda en 97 > 96: el algoritmo lo preferiría aunque no sea factible.

### 3. ¿Qué pasa si λ es demasiado grande?

La penalización es tan fuerte que las soluciones inválidas caen bruscamente en aptitud y
casi nunca son seleccionadas. Se asegura cumplir la restricción, pero si λ es extremo
(por ejemplo 50) se pierde exploración en las regiones **cercanas al límite del presupuesto**
(donde suele estar el óptimo) y baja la diversidad de la población. En el ejemplo, con λ = 50
el inválido queda en 48, muy lejos de la mejor válida, y el algoritmo solo "ve" soluciones
muy conservadoras.

### 4. ¿Cuál es el valor adecuado?

El suficiente para que **ninguna solución inválida supere a la mejor válida**. En este
problema λ = 5 (el sugerido por el taller) cumple: deja al inválido de ejemplo en 93, por
debajo de 96. Regla general: λ debe ser mayor que el beneficio máximo por unidad de costo
excedida. Nota: con λ = 2 el inválido iguala a la mejor válida (96 = 96), así que conviene
`λ > 2`.

## Evidencia de las afirmaciones (con los resultados)

Todas las afirmaciones anteriores se respaldan con la ejecución de `punto2.py`
(seed 42), disponible en texto en `resultados_punto2.txt` y en tablas en los CSV
de esta carpeta (GitHub los visualiza como tablas).

### Afirmación → resultado que la valida

| # | Afirmación del README | Resultado que la valida | Fuente |
|---|---|---|---|
| 1 | Cada unidad de λ se descuenta del beneficio por unidad de exceso | Inválido (B=98, exceso=1): λ=0→98.00, λ=1→97.00, λ=5→93.00, λ=50→48.00 | `resultados_punto2_lambda.csv` |
| 2 | λ pequeño → el inválido supera a la mejor válida | λ=1: **97.00 > 96.00** | `resultados_punto2_lambda.csv` |
| 3 | λ grande → el inválido cae bruscamente | λ=50: **48.00**, muy por debajo de 96.00 | `resultados_punto2_lambda.csv` |
| 4 | λ=5 deja al inválido por debajo de la mejor válida | λ=5: **93.00 < 96.00** | `resultados_punto2_lambda.csv` |
| 5 | Regla λ > 2 (con λ=2 el inválido iguala a la mejor válida) | λ=2: **96.00 = 96.00**; λ=3: **95.00 < 96.00** | `resultados_punto2_lambda.csv` |
| 6 | La misma fórmula se aplicó en la tabla de la población | Individuo #4 `1011101010`: B=98, C=51 → aptitud = 98 − 5·1 = **93.00** ✓ | `resultados_punto2_poblacion.csv` |
| 7 | 13 de 20 soluciones son válidas | **13/20 (65.0 %)** | `resultados_punto2.txt` |
| 8 | La mejor válida gana 96 | Individuo #8 `0111001011` (P2, P3, P4, P7, P9, P10; costo 50, beneficio 96 → aptitud 96.00) | `resultados_punto2_poblacion.csv` |
| 9 | Aptitud promedio de la población = 65.95 | **65.95** (suma 1319.00 / 20) | `resultados_punto2.txt` |

### Datos completos

- [`resultados_punto2_poblacion.csv`](resultados_punto2_poblacion.csv): los 20 individuos con cromosoma, proyectos seleccionados, costo, beneficio, aptitud y validez.
- [`resultados_punto2_lambda.csv`](resultados_punto2_lambda.csv): sensibilidad de la aptitud del inválido de ejemplo para distintos valores de λ.

## Convenciones del proyecto

- Código en español, con comentarios y docstrings.
- Semilla fija (`random.seed(42)`) para resultados reproducibles.
- Commits atómicos con mensajes convencionales.

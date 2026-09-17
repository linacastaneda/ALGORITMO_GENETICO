# Punto 2 — Población inicial y función de aptitud

**Curso:** Introducción a la Inteligencia Artificial
**Taller:** Diseño e implementación de un algoritmo genético (Python)

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
punto 2/
├── punto2.py               # Código: población inicial + función de aptitud (λ)
├── resultados_punto2.txt   # Salida de una ejecución (seed 42)
├── ejercicios_punto2.md    # Desarrollo del punto 2 (ejercicio + análisis de λ)
└── README.md               # Este archivo (dudas resueltas del punto)
```

## Ejecución

```bash
python -X utf8 "punto 2/punto2.py"
```

Solo requiere Python estándar. El script regenera `resultados_punto2.txt` automáticamente.

---

## Dudas del punto 2 (respondidas)

### 1. ¿Qué significa λ (lambda)?

λ es un número que elegís vos y que **controla qué tan fuerte se castiga a las soluciones
que se pasan del presupuesto**. Es el "precio" que se le cobra por **cada unidad de exceso**
sobre el presupuesto:

```
fitness(X) = B(X)                           si C(X) ≤ 50
fitness(X) = B(X) − λ · (C(X) − 50)         si C(X) > 50
```

Ejemplo con los datos reales de la ejecución:
- Un individuo inválido con beneficio **98** que gasta **51** (exceso = 1).
- La mejor solución válida obtiene **96**.

| λ | Aptitud del inválido | Resultado |
|---|---|---|
| 1 | 98 − 1×1 = **97** | Supera a la mejor válida (96) → conviene violar el presupuesto |
| 5 | 98 − 5×1 = **93** | Queda por debajo de la mejor válida → gastar de más "no conviene" |

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

## Convenciones del proyecto

- Código en español, con comentarios y docstrings.
- Semilla fija (`random.seed(42)`) para resultados reproducibles.
- Commits atómicos con mensajes convencionales.
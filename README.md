# Algoritmo Genético — Taller de optimización de proyectos

**Curso:** Introducción a la Inteligencia Artificial
**Taller:** Diseño e implementación de un algoritmo genético (Python)

## Problema

Una organización dispone de un presupuesto de **50 unidades monetarias** para financiar
proyectos de innovación. Cada proyecto (P1–P10) tiene un costo y un beneficio estimado.
Objetivo: seleccionar el conjunto de proyectos que maximice el beneficio sin superar el
presupuesto.

- Representación: cromosoma binario de 10 genes (`x_i = 1` si se selecciona el proyecto `i`).
- Restricción: `C(X) <= 50`. Se maximiza `B(X)`.

## Estructura del repositorio

```
ALGORITMO_GENETICO/
├── punto 2/
│   ├── punto2.py               # Población inicial + función de aptitud (λ)
│   ├── resultados_punto2.txt   # Salida de una ejecución (seed 42)
│   └── ejercicios_punto2.md    # Explicación del punto 2 (ejercicio + efecto de λ)
└── README.md
```

## Ejecución

Para corrientes de Python con Unicode compatible:

```bash
# Punto 2: población inicial y función de aptitud
python -X utf8 "punto 2/punto2.py"
```

El script genera `resultados_punto2.txt` automáticamente en su carpeta.
Requiere únicamente Python estándar (no hay dependencias externas).

## Puntos del taller

| Punto | Estado |
|---|---|
| 1. Formulación del problema | Pendiente |
| 2. Población y función de aptitud | **Completado** |
| 3. Operadores genéticos | Pendiente |
| 4. Algoritmo genético completo | Pendiente |
| 5. Experimentación y análisis | Pendiente |

## Convenciones del proyecto

- Código en español, con comentarios y docstrings.
- Semilla fija (`random.seed(42)`) para resultados reproducibles.
- Commits atómicos con mensajes convencionales.
# Punto 2 – Población y función de aptitud

**Curso:** Introducción a la Inteligencia Artificial · Taller de Algoritmos Genéticos
**Problema:** Selección óptima de proyectos (presupuesto máximo = 50)
**Archivos de esta carpeta:**
- `punto2_poblacion_aptitud.py` — código fuente comentado.
- `resultados_punto2.txt` — salida completa de una ejecución (`random.seed(42)`).

---

## 1. Lo que se implementó

| Requisito del punto | Implementación |
|---|---|
| Generar población inicial aleatoria | `generar_individuo()` y `generar_poblacion(N=20)` |
| Función de aptitud con penalización | `calcular_aptitud(cromosoma, lam=5)` |
| Mostrar cromosoma y proyectos seleccionados | `proyectos_seleccionados()` |
| Costo total | `calcular_costo()` |
| Beneficio total | `calcular_beneficio()` |
| Indicación de solución válida | `costo <= 50` (columna **Valida**) |

**Representación:** cada individuo es un cromosoma binario de 10 genes, uno por proyecto (`x_i = 1` si se selecciona, `0` si no).

**Función de aptitud usada:**

```
fitness(X) = B(X)                    si C(X) <= 50
fitness(X) = B(X) - lam * (C(X) - 50)   si C(X) > 50
```

con `lam = 5`. Así se premia el mayor beneficio y se penaliza a quien se pasa del presupuesto.

---

## 2. Resultados de la población inicial (N = 20, λ = 5)

Detalle completo en `resultados_punto2.txt`. Resumen de la ejecución:

| Métrica | Valor |
|---|---|
| Individuos generados | 20 |
| Soluciones válidas | 13 de 20 (65 %) |
| Aptitud promedio de la población | 65,95 |
| Suma de aptitudes | 1319,00 |
| Mejor solución válida | `0111001011` → P2, P3, P4, P7, P9, P10 |
| Costo / Beneficio de la mejor válida | 50 / **96** |

Ejemplos de la tabla generada:

| Cromosoma | Proyectos | Costo | Beneficio | Aptitud | Válida |
|---|---|---|---|---|---|
| `0010000010` | P3, P9 | 16 | 32 | 32,00 | SI |
| `0011100100` | P3, P4, P5, P8 | 38 | 73 | 73,00 | SI |
| `1110011011` | P1, P2, P3, P6, P7 | 68 | 133 | 43,00 | NO |
| `0111001011` | P2, P3, P4, P7, P9, P10 | 50 | 96 | 96,00 | SI |

Se observa que los individuos **inválidos** (costo > 50) quedan con aptitud muy por debajo de su beneficio, porque se les descuenta `λ·(C − 50)`.

---

## 3. Efecto del parámetro de penalización λ

El programa toma un individuo inválido de la población generada y calcula su aptitud para distintos valores de λ:

- Individuo de ejemplo: `1011101010` → P1, P3, P4, P5, P7, P9
- Costo = 51 (exceso = 1), Beneficio = 98
- Mejor aptitud entre soluciones válidas = **96,00**

| λ | Aptitud del inválido | Observación |
|---|---|---|
| 0 | 98,00 | igual a su beneficio (sin penalización) |
| 1 | 97,00 | supera la mejor válida |
| 2 | 96,00 | iguala la mejor válida |
| 3 | 95,00 | queda por debajo de la mejor válida |
| **5** | **93,00** | queda por debajo de la mejor válida |
| 10 | 88,00 | queda por debajo |
| 20 | 78,00 | queda por debajo |
| 50 | 48,00 | queda por debajo |

### Explicación

- **λ demasiado pequeño (p. ej. 0, 1):** la penalización es débil. Una solución que excede el presupuesto puede quedar con **mayor aptitud que la mejor solución válida**. El algoritmo genético tenderá a favorecer e incluso converger a soluciones **inválidas** que violan la restricción (exceso de presupuesto). El mejor individuo reportado podría no ser factible.
- **λ demasiado grande (p. ej. 20, 50):** la penalización es tan fuerte que las soluciones inválidas caen abruptamente en aptitud y prácticamente nunca son seleccionadas. La restricción se cumple fácilmente, pero si λ es extremo, el algoritmo deja de explorar las regiones **cercanas al límite del presupuesto** (donde suele estar el óptimo) y se pierde diversidad en la población.
- **Valor adecuado:** debe ser lo bastante grande para que **ninguna solución inválida supere a la mejor válida**. En el ejemplo, el inválido (98 de beneficio, exceso 1) supera/iguala a 96 mientras `λ < 2`, por lo que conviene `λ > 2`. El valor sugerido del taller, **λ = 5**, cumple: deja al inválido en 93,00, por debajo de 96,00. En general, una regla segura es elegir λ mayor que el beneficio máximo por unidad de costo excedida.

---

## 4. Conclusión del punto

Con `N = 20` y `λ = 5` se genera una población diversa (13/20 soluciones válidas). La función de aptitud penaliza correctamente el exceso de presupuesto y permite comparar todas las soluciones, válidas e inválidas, en una misma escala. El parámetro `λ` controla la severidad de la penalización: muy pequeño → soluciones inválidas ganan; muy grande → pérdida de exploración.
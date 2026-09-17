# -*- coding: utf-8 -*-
"""
Punto 2. Poblacion y funcion de aptitud
Taller: Algoritmos geneticos - Introduccion a la Inteligencia Artificial

Problema: seleccion optima de proyectos.
Presupuesto maximo disponible: 50 unidades monetarias.
Objetivo: maximizar el beneficio total B(X) sin superar el presupuesto C(X) <= 50.

Este programa:
  1. Genera una poblacion inicial aleatoria de N = 20 cromosomas binarios.
  2. Calcula costo, beneficio y aptitud de cada individuo.
  3. Penaliza las soluciones que exceden el presupuesto usando un parametro lambda.
  4. Muestra, para cada individuo: cromosoma, proyectos seleccionados,
     costo total, beneficio total, valor de aptitud y si la solucion es valida.
  5. Analiza el efecto de variar la penalizacion lambda sobre una solucion invalida.

Ejecucion:
    python punto2_poblacion_aptitud.py
"""

import random

# ---------------------------------------------------------------------------
# Datos del problema: proyectos, costos y beneficios
# ---------------------------------------------------------------------------
PROYECTOS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]
COSTOS = [12, 7, 11, 8, 9, 14, 6, 10, 5, 13]
BENEFICIOS = [24, 13, 23, 15, 16, 28, 11, 19, 9, 25]
PRESUPUESTO = 50
N_GENES = len(PROYECTOS)

# Semilla para resultados reproducibles
random.seed(42)


# ---------------------------------------------------------------------------
# Representacion y poblacion inicial
# ---------------------------------------------------------------------------
def generar_individuo():
    """Genera un cromosoma binario aleatorio de 10 genes (0 o 1)."""
    return [random.randint(0, 1) for _ in range(N_GENES)]  


def generar_poblacion(n=20):
    """Genera una poblacion inicial de n cromosomas binarios aleatorios."""
    return [generar_individuo() for _ in range(n)]


# ---------------------------------------------------------------------------
# Evaluacion: costo, beneficio y aptitud
# ---------------------------------------------------------------------------
def calcular_costo(cromosoma):
    """Costo total C(X) = sum(c_i * x_i)."""
    return sum(x * c for x, c in zip(cromosoma, COSTOS))


def calcular_beneficio(cromosoma):
    """Beneficio total B(X) = sum(b_i * x_i)."""
    return sum(x * b for x, b in zip(cromosoma, BENEFICIOS))


def calcular_aptitud(cromosoma, lam=5):
    """
    Funcion de aptitud con penalizacion por exceder el presupuesto:
        fitness(X) = B(X),                      si C(X) <= 50
        fitness(X) = B(X) - lam * (C(X) - 50),  si C(X) > 50
    """
    costo = calcular_costo(cromosoma)
    beneficio = calcular_beneficio(cromosoma)
    if costo <= PRESUPUESTO:
        return float(beneficio)
    return float(beneficio - lam * (costo - PRESUPUESTO))


def es_valida(cromosoma):
    """Indica si el individuo respeta el presupuesto (C(X) <= 50)."""
    return calcular_costo(cromosoma) <= PRESUPUESTO


def proyectos_seleccionados(cromosoma):
    """Devuelve la lista de proyectos seleccionados por el cromosoma."""
    return [PROYECTOS[i] for i, x in enumerate(cromosoma) if x == 1]


# ---------------------------------------------------------------------------
# Reporte
# ---------------------------------------------------------------------------
def construir_reporte(poblacion, lam=5):
    """Construye el reporte de la poblacion: detalle por individuo + resumen."""
    lineas = []
    lineas.append("=" * 78)
    lineas.append("PUNTO 2 - POBLACION INICIAL Y FUNCION DE APTITUD")
    lineas.append("Problema: seleccion optima de proyectos | Presupuesto = 50")
    lineas.append("Parametros: N = %d, lambda = %d" % (len(poblacion), lam))
    lineas.append("=" * 78)
    cab = "%-3s | %-17s | %-18s | %6s | %8s | %8s | %-4s"
    lineas.append(cab % ("#", "Cromosoma (x1..x10)", "Proyectos", "Costo", "Beneficio", "Aptitud", "Valida"))
    lineas.append("-" * 78)

    n_validas = 0
    aptitudes = []
    mejor_valida = None  # individuo valido con mayor beneficio (aptitud)

    for i, crom in enumerate(poblacion, start=1):
        costo = calcular_costo(crom)
        beneficio = calcular_beneficio(crom)
        aptitud = calcular_aptitud(crom, lam)
        valida = costo <= PRESUPUESTO
        prods = ", ".join(proyectos_seleccionados(crom)) if valida or True else ""
        if not prods:
            prods = "-"
        if valida:
            n_validas += 1
            if mejor_valida is None or beneficio > mejor_valida[1]:
                mejor_valida = (crom, beneficio, costo)
        aptitudes.append(aptitud)
        crom_string = "".join(str(g) for g in crom)
        lineas.append("%-3d | %-17s | %-18s | %6d | %8d | %8.2f | %s" % (
            i, crom_string, prods[:18], costo, beneficio, aptitud,
            "SI" if valida else "NO"))

    lineas.append("-" * 78)
    suma = sum(aptitudes)
    prom = suma / len(aptitudes) if aptitudes else 0.0
    lineas.append("Resumen:")
    lineas.append("  Poblacion: %d individuos" % len(poblacion))
    lineas.append("  Soluciones validas: %d de %d (%.1f%%)"
                  % (n_validas, len(poblacion), 100.0 * n_validas / len(poblacion)))
    lineas.append("  Aptitud promedio de la poblacion: %.2f" % prom)
    lineas.append("  Suma de aptitudes: %.2f" % suma)
    if mejor_valida is not None:
        mejor_crom, mejor_ben, mejor_cost = mejor_valida
        lineas.append("  Mejor solucion valida encontrada:")
        lineas.append("    Cromosoma : %s" % "".join(str(g) for g in mejor_crom))
        lineas.append("    Proyectos : %s" % ", ".join(proyectos_seleccionados(mejor_crom)))
        lineas.append("    Costo     : %d" % mejor_cost)
        lineas.append("    Beneficio : %d" % mejor_ben)
        lineas.append("    Aptitud   : %.2f" % calcular_aptitud(mejor_crom, lam))
    return "\n".join(lineas)


# ---------------------------------------------------------------------------
# Analisis del efecto de lambda sobre una solucion invalida
# ---------------------------------------------------------------------------
def analisis_lambda(poblacion, lam_referencia=5):
    """Muestra como cambia la aptitud de un individuo invalido al variar lambda."""
    lineas = []
    lineas.append("")
    lineas.append("=" * 78)
    lineas.append("ANALISIS: EFECTO DEL PARAMETRO DE PENALIZACION LAMBDA")
    lineas.append("=" * 78)

    # Buscar el primer individuo que exceda el presupuesto
    invalido = None
    for crom in poblacion:
        if calcular_costo(crom) > PRESUPUESTO:
            invalido = crom
            break

    # Mejor aptitud entre individuos validos (con lambda de referencia)
    mejor_apt_valida = max(
        calcular_aptitud(c, lam_referencia) for c in poblacion if es_valida(c))

    if invalido is None:
        lineas.append("No se encontro ningun individuo invalido en la poblacion.")
        return "\n".join(lineas)

    costo = calcular_costo(invalido)
    beneficio = calcular_beneficio(invalido)
    exceso = costo - PRESUPUESTO
    prods = ", ".join(proyectos_seleccionados(invalido))
    lineas.append("Individuo invalido de ejemplo:")
    lineas.append("  Cromosoma : %s" % "".join(str(g) for g in invalido))
    lineas.append("  Proyectos : %s" % prods)
    lineas.append("  Costo     : %d (exceso de %d sobre el presupuesto)" % (costo, exceso))
    lineas.append("  Beneficio : %d" % beneficio)
    lineas.append("  Mejor aptitud entre soluciones VALIDAS: %.2f" % mejor_apt_valida)
    lineas.append("")
    lineas.append("  lambda | aptitud del invalido | observacion")
    lineas.append("  -------|----------------------|---------------------------------------")
    for lam in [0, 1, 2, 3, 5, 10, 20, 50]:
        apt = beneficio - lam * exceso  # equivalente a calcular_aptitud con lam
        obs = "igual que su beneficio (sin penalizacion)" if lam == 0 else ""
        if lam > 0 and apt > mejor_apt_valida:
            obs = "supera la mejor aptitud valida"
        elif lam > 0 and apt == mejor_apt_valida:
            obs = "igual a la mejor aptitud valida"
        elif lam > 0:
            obs = "queda por debajo de la mejor aptitud valida"
        lineas.append("  %6d | %20.2f | %s" % (lam, apt, obs))
    lineas.append("")
    lineas.append("Con lambda = %d, la aptitud del invalido es %.2f; la mejor valida es %.2f."
                  % (lam_referencia,
                     beneficio - lam_referencia * exceso,
                     mejor_apt_valida))
    lineas.append("")
    lineas.append("Explicacion:")
    lineas.append("  - lambda PEQUENO (p. ej. 0, 1): la penalizacion es debil. Una solucion")
    lineas.append("    que excede el presupuesto puede mostrar una aptitud mayor que la de")
    lineas.append("    la mejor solucion valida, por lo que el algoritmo genetico tendera")
    lineas.append("    a favorecer soluciones invalidas y podria converger a una solucion")
    lineas.append("    que no respeta la restriccion.")
    lineas.append("  - lambda GRANDE (p. ej. 20, 50): la penalizacion es fuerte. Las soluciones")
    lineas.append("    invalidas caen bruscamente en aptitud y casi nunca son seleccionadas.")
    lineas.append("    Se favorece el cumplimiento de la restriccion, aunque una penalizacion")
    lineas.append("    extrema reduce la exploracion de regiones cercanas al limite del")
    lineas.append("    presupuesto y puede perjudicar la diversidad de la poblacion.")
    lineas.append("  - Valor adecuado: el suficiente para que ninguna solucion invalida supere")
    lineas.append("    a la mejor valida. En este problema, con lambda = 5 el invalido de")
    lineas.append("    ejemplo (%d de beneficio, %d de exceso) obtiene aptitud %.2f,"
                  % (beneficio, exceso, beneficio - lam_referencia * exceso))
    lineas.append("    mientras que la mejor valida alcanza %.2f." % mejor_apt_valida)
    return "\n".join(lineas)


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def main():
    lam = 5
    n = 20

    poblacion = generar_poblacion(n)

    reporte = construir_reporte(poblacion, lam)
    reporte += "\n" + analisis_lambda(poblacion, lam_referencia=lam)

    print(reporte)

    # Guardar resultados en un archivo (parte del entregable)
    with open("resultados_punto2.txt", "w", encoding="utf-8") as f:
        f.write(reporte + "\n")
    print("\n[OK] Resultados guardados en resultados_punto2.txt")


if __name__ == "__main__":
    main()
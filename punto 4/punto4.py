# -*- coding: utf-8 -*-
"""
Punto 4. Algoritmo genetico completo
Taller: Algoritmos geneticos - Introduccion a la Inteligencia Artificial

Integra los componentes de los puntos anteriores en un unico algoritmo genetico:
  1. Generar la poblacion inicial.
  2. Evaluar la aptitud de todos los individuos.
  3. Seleccionar los padres (torneo de tamano 3).
  4. Aplicar cruce de un punto y mutacion binaria.
  5. Construir la nueva poblacion.
  6. Conservar el mejor individuo mediante elitismo.
  7. Repetir hasta el criterio de terminacion (num. de generaciones).

Configuracion inicial (tabla del taller):
  Tamano de poblacion ......... 20
  Numero de generaciones ...... 100
  Probabilidad de cruce ....... 0.80
  Probabilidad de mutacion .... 0.05
  Tamano del torneo ........... 3
  Numero de individuos elite .. 1
  Penalizacion lambda ......... 5

El programa registra en cada generacion: numero de generacion, mejor aptitud,
beneficio y costo de la mejor solucion, su cromosoma y la aptitud promedio de la
poblacion. Al finalizar presenta los proyectos seleccionados por la mejor solucion.

Ejecucion:
    python -X utf8 punto4.py
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

# Parametros del algoritmo (configuracion inicial del taller)
CONFIG = {
    "tamano_poblacion": 20,
    "num_generaciones": 100,
    "prob_cruce": 0.80,
    "prob_mutacion": 0.05,
    "tamano_torneo": 3,
    "numero_elite": 1,
    "lambda": 5,
}

# Semilla para resultados reproducibles
random.seed(42)


# ---------------------------------------------------------------------------
# Representacion, poblacion inicial y evaluacion (punto 2)
# ---------------------------------------------------------------------------
def generar_individuo():
    """Genera un cromosoma binario aleatorio de 10 genes (0 o 1)."""
    return [random.randint(0, 1) for _ in range(N_GENES)]


def generar_poblacion(n=20):
    """Genera una poblacion inicial de n cromosomas binarios aleatorios."""
    return [generar_individuo() for _ in range(n)]


def calcular_costo(cromosoma):
    """Costo total C(X) = sum(c_i * x_i)."""
    return sum(x * c for x, c in zip(cromosoma, COSTOS))


def calcular_beneficio(cromosoma):
    """Beneficio total B(X) = sum(b_i * x_i)."""
    return sum(x * b for x, b in zip(cromosoma, BENEFICIOS))


def calcular_aptitud(cromosoma, lam=5):
    """Aptitud: B(X) si C(X) <= 50; B(X) - lam*(C(X) - 50) si excede."""
    costo = calcular_costo(cromosoma)
    beneficio = calcular_beneficio(cromosoma)
    if costo <= PRESUPUESTO:
        return float(beneficio)
    return float(beneficio - lam * (costo - PRESUPUESTO))


def proyectos_seleccionados(cromosoma):
    """Nombres de los proyectos seleccionados por el cromosoma."""
    return [PROYECTOS[i] for i, x in enumerate(cromosoma) if x == 1]


# ---------------------------------------------------------------------------
# Operadores geneticos (punto 3)
# ---------------------------------------------------------------------------
def seleccionar_padre(poblacion, aptitudes, tamano_torneo=3):
    """Seleccion por torneo: elige K individuos al azar y devuelve el de mayor aptitud."""
    participantes = random.sample(range(len(poblacion)), tamano_torneo)
    mejor = max(participantes, key=lambda i: aptitudes[i])
    return poblacion[mejor]


def cruzar(padre1, padre2, prob_cruce=0.80):
    """Cruce de un punto: intercambia los segmentos desde una posicion aleatoria."""
    if random.random() < prob_cruce:
        punto = random.randint(1, N_GENES - 1)
        hijo1 = padre1[:punto] + padre2[punto:]
        hijo2 = padre2[:punto] + padre1[punto:]
        return hijo1, hijo2
    return list(padre1), list(padre2)


def mutar(cromosoma, prob_mutacion=0.05):
    """Mutacion binaria: cada gen cambia (0<->1) con probabilidad pm."""
    return [1 - g if random.random() < prob_mutacion else g for g in cromosoma]


# ---------------------------------------------------------------------------
# Algoritmo genetico completo (punto 4)
# ---------------------------------------------------------------------------
def ejecutar_algoritmo_genetico(config=None):
    """
    Ejecuta el algoritmo genetico completo y devuelve el historial de cada
    generacion junto con la mejor solucion global encontrada.

    Returns:
        historial: lista de tuplas (gen, mejor_aptitud, mejor_beneficio,
                   mejor_costo, mejor_cromosoma, aptitud_promedio).
        mejor_global: cromosoma con la mejor aptitud de todo el proceso.
        mejor_global_apt: valor de aptitud de la mejor solucion.
        gen_mejor: generacion en la que aparecio la mejor solucion.
    """
    parametros = dict(CONFIG if config is None else config)
    n = parametros["tamano_poblacion"]
    generaciones = parametros["num_generaciones"]
    prob_cruce = parametros["prob_cruce"]
    prob_mutacion = parametros["prob_mutacion"]
    tamano_torneo = parametros["tamano_torneo"]
    numero_elite = parametros["numero_elite"]
    lam = parametros["lambda"]

    poblacion = generar_poblacion(n)
    historial = []

    mejor_global = None
    mejor_global_apt = -float("inf")
    gen_mejor = 0

    for gen in range(1, generaciones + 1):
        # 2. Evaluar la aptitud de todos los individuos
        aptitudes = [calcular_aptitud(c, lam) for c in poblacion]

        idx_mejor = max(range(n), key=lambda i: aptitudes[i])
        mejor_actual = poblacion[idx_mejor]
        apt_actual = aptitudes[idx_mejor]
        benef_actual = calcular_beneficio(mejor_actual)
        costo_actual = calcular_costo(mejor_actual)
        promedio = sum(aptitudes) / n

        # Registrar la generacion
        historial.append((gen, apt_actual, benef_actual, costo_actual,
                          list(mejor_actual), promedio))

        # Actualizar el mejor global si corresponde
        if apt_actual > mejor_global_apt:
            mejor_global_apt = apt_actual
            mejor_global = list(mejor_actual)
            gen_mejor = gen

        # 6. Elitismo: conservar los mejores individuos intactos
        orden = sorted(range(n), key=lambda i: aptitudes[i], reverse=True)
        elite = [list(poblacion[i]) for i in orden[:numero_elite]]

        # 3, 4 y 5: seleccionar padres, cruzar y mutar para la nueva poblacion
        nueva_poblacion = []
        while len(nueva_poblacion) < n - numero_elite:
            p1 = seleccionar_padre(poblacion, aptitudes, tamano_torneo)
            p2 = seleccionar_padre(poblacion, aptitudes, tamano_torneo)
            h1, h2 = cruzar(p1, p2, prob_cruce)
            nueva_poblacion.append(mutar(h1, prob_mutacion))
            nueva_poblacion.append(mutar(h2, prob_mutacion))
            if len(nueva_poblacion) > n - numero_elite:
                nueva_poblacion = nueva_poblacion[:n - numero_elite]

        poblacion = elite + nueva_poblacion

    return historial, mejor_global, mejor_global_apt, gen_mejor


# ---------------------------------------------------------------------------
# Reporte
# ---------------------------------------------------------------------------
def construir_reporte(config=None):
    """Ejecuta el AG y construye el reporte completo del punto 4."""
    parametros = dict(CONFIG if config is None else config)
    historial, mejor, mejor_apt, gen_mejor = ejecutar_algoritmo_genetico(parametros)

    lineas = []
    lineas.append("=" * 82)
    lineas.append("PUNTO 4 - ALGORITMO GENETICO COMPLETO")
    lineas.append("Problema: seleccion optima de proyectos | Presupuesto = 50")
    lineas.append("Configuracion:")
    lineas.append("  Poblacion: %d | Generaciones: %d | Cruce: %.2f | Mutacion: %.2f"
                  % (parametros["tamano_poblacion"], parametros["num_generaciones"],
                     parametros["prob_cruce"], parametros["prob_mutacion"]))
    lineas.append("  Torneo: %d | Elite: %d | Lambda: %d"
                  % (parametros["tamano_torneo"], parametros["numero_elite"],
                     parametros["lambda"]))
    lineas.append("=" * 82)
    lineas.append("Registro por generacion:")
    cab = "%-4s | %12s | %9s | %6s | %-17s | %14s" % (
        "Gen", "Mejor aptitud", "Beneficio", "Costo", "Cromosoma", "Apt. promedio")
    lineas.append(cab)
    lineas.append("-" * 82)

    for (gen, apt, ben, cos, crom, prom) in historial:
        lineas.append("%-4d | %12.2f | %9d | %6d | %-17s | %14.2f"
                      % (gen, apt, ben, cos, "".join(str(g) for g in crom), prom))

    lineas.append("-" * 82)

    mejor_ben = calcular_beneficio(mejor)
    mejor_cos = calcular_costo(mejor)
    mejor_valida = mejor_cos <= PRESUPUESTO
    lineas.append("")
    lineas.append("MEJOR SOLUCION ENCONTRADA:")
    lineas.append("  Generacion de aparicion : %d" % gen_mejor)
    lineas.append("  Cromosoma               : %s" % "".join(str(g) for g in mejor))
    lineas.append("  Proyectos seleccionados : %s" % ", ".join(proyectos_seleccionados(mejor)))
    lineas.append("  Costo total             : %d" % mejor_cos)
    lineas.append("  Beneficio total         : %d" % mejor_ben)
    lineas.append("  Aptitud                 : %.2f" % mejor_apt)
    lineas.append("  Solucion valida         : %s" % ("SI" if mejor_valida else "NO"))
    lineas.append("")
    lineas.append("Aptitud promedio de la ultima generacion: %.2f" % historial[-1][5])
    return "\n".join(lineas), mejor


def main():
    reporte, _mejor = construir_reporte()
    print(reporte)

    with open("resultados_punto4.txt", "w", encoding="utf-8") as f:
        f.write(reporte + "\n")
    print("\n[OK] Resultados guardados en resultados_punto4.txt")


if __name__ == "__main__":
    main()
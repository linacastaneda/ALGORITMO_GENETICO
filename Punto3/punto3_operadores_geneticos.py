import random


# ============================================================
# PUNTO 3 - OPERADORES GENÉTICOS
# Problema: Selección óptima de proyectos
# Presupuesto máximo = 50
# ============================================================


# ============================================================
# DATOS DEL PROBLEMA
# ============================================================

PROYECTOS = [
    "P1", "P2", "P3", "P4", "P5",
    "P6", "P7", "P8", "P9", "P10"
]

COSTOS = [
    12, 7, 11, 8, 9,
    14, 6, 10, 5, 13
]

BENEFICIOS = [
    24, 13, 23, 15, 16,
    28, 11, 19, 9, 25
]

PRESUPUESTO = 50
LAMBDA = 5
N_GENES = len(PROYECTOS)

# Probabilidad de mutación solicitada
PROB_MUTACION = 0.05

# Semilla para obtener resultados reproducibles
random.seed(42)


# ============================================================
# FUNCIONES DEL PUNTO 2 QUE NECESITAMOS
# ============================================================

def generar_individuo():
    """
    Genera un cromosoma binario de 10 genes.

    1 = proyecto seleccionado
    0 = proyecto no seleccionado
    """
    return [random.randint(0, 1) for _ in range(N_GENES)]


def generar_poblacion(n=20):
    """
    Genera una población de n individuos.
    """
    return [generar_individuo() for _ in range(n)]


def calcular_costo(cromosoma):
    """
    Calcula el costo total de los proyectos seleccionados.
    """
    return sum(
        gen * costo
        for gen, costo in zip(cromosoma, COSTOS)
    )


def calcular_beneficio(cromosoma):
    """
    Calcula el beneficio total de los proyectos seleccionados.
    """
    return sum(
        gen * beneficio
        for gen, beneficio in zip(cromosoma, BENEFICIOS)
    )


def calcular_aptitud(cromosoma, lam=LAMBDA):
    """
    Calcula la aptitud del individuo.

    Si el costo está dentro del presupuesto:
        aptitud = beneficio

    Si supera el presupuesto:
        aptitud = beneficio - lambda * exceso
    """

    costo = calcular_costo(cromosoma)
    beneficio = calcular_beneficio(cromosoma)

    if costo <= PRESUPUESTO:
        return beneficio

    exceso = costo - PRESUPUESTO

    return beneficio - lam * exceso


def es_valida(cromosoma):
    """
    Verifica si el individuo cumple con el presupuesto.
    """
    return calcular_costo(cromosoma) <= PRESUPUESTO


def proyectos_seleccionados(cromosoma):
    """
    Devuelve los proyectos que tienen gen = 1.
    """
    return [
        proyecto
        for proyecto, gen in zip(PROYECTOS, cromosoma)
        if gen == 1
    ]


# ============================================================
# FUNCIÓN AUXILIAR
# ============================================================

def cromosoma_texto(cromosoma):
    """
    Convierte una lista de genes en una cadena.

    Ejemplo:
    [1, 0, 1, 1] -> 1011
    """
    return "".join(map(str, cromosoma))


# ============================================================
# PUNTO 3.1 - SELECCIÓN POR TORNEO
# ============================================================

def seleccionar_padre(poblacion, tam_torneo=3):
    """
    Selecciona un padre mediante torneo.

    Se seleccionan aleatoriamente 3 individuos
    y gana el que tenga la mayor aptitud.

    Retorna:
        ganador, torneo
    """

    torneo = random.sample(poblacion, tam_torneo)

    ganador = max(
        torneo,
        key=lambda individuo: calcular_aptitud(individuo)
    )

    return ganador, torneo


# ============================================================
# PUNTO 3.2 - CRUCE DE UN PUNTO
# ============================================================

def cruzar(padre1, padre2):
    """
    Realiza un cruce de un punto entre dos padres.

    Se selecciona una posición de corte y se intercambian
    las partes posteriores de los cromosomas.

    Retorna:
        hijo1, hijo2, punto_cruce
    """

    punto_cruce = random.randint(1, N_GENES - 1)

    hijo1 = (
        padre1[:punto_cruce]
        + padre2[punto_cruce:]
    )

    hijo2 = (
        padre2[:punto_cruce]
        + padre1[punto_cruce:]
    )

    return hijo1, hijo2, punto_cruce


# ============================================================
# PUNTO 3.3 - MUTACIÓN BINARIA
# ============================================================

def mutar(cromosoma, pm=PROB_MUTACION):
    """
    Aplica mutación binaria.

    Cada gen tiene una probabilidad de 0.05 de mutar.

    Si muta:
        0 -> 1
        1 -> 0

    Retorna:
        cromosoma_mutado, posiciones_mutadas
    """

    cromosoma_mutado = cromosoma.copy()
    posiciones_mutadas = []

    for i in range(len(cromosoma_mutado)):

        if random.random() < pm:

            cromosoma_mutado[i] = 1 - cromosoma_mutado[i]

            # Se guarda la posición comenzando desde 1
            posiciones_mutadas.append(i + 1)

    return cromosoma_mutado, posiciones_mutadas


# ============================================================
# MOSTRAR INFORMACIÓN DE UN INDIVIDUO
# ============================================================

def mostrar_individuo(nombre, cromosoma):

    costo = calcular_costo(cromosoma)
    beneficio = calcular_beneficio(cromosoma)
    aptitud = calcular_aptitud(cromosoma)

    proyectos = proyectos_seleccionados(cromosoma)

    print(f"{nombre}:")
    print(f"  Cromosoma : {cromosoma_texto(cromosoma)}")
    print(f"  Proyectos : {', '.join(proyectos)}")
    print(f"  Costo     : {costo}")
    print(f"  Beneficio : {beneficio}")
    print(f"  Aptitud   : {aptitud:.2f}")
    print(f"  Válida    : {'SI' if es_valida(cromosoma) else 'NO'}")


# ============================================================
# DEMOSTRACIÓN DEL PUNTO 3
# ============================================================

def demostracion_punto3():

    print("=" * 70)
    print("PUNTO 3 - OPERADORES GENÉTICOS")
    print("=" * 70)

    # --------------------------------------------------------
    # 1. GENERAR POBLACIÓN
    # --------------------------------------------------------

    poblacion = generar_poblacion(20)

    print("\nPOBLACIÓN INICIAL")
    print("-" * 70)
    print(f"Cantidad de individuos: {len(poblacion)}")

    # --------------------------------------------------------
    # 2. SELECCIÓN DEL PADRE 1
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("1. SELECCIÓN POR TORNEO")
    print("=" * 70)

    padre1, torneo1 = seleccionar_padre(
        poblacion,
        tam_torneo=3
    )

    print("\nTorneo para seleccionar PADRE 1:")

    for i, individuo in enumerate(torneo1, start=1):

        print(
            f"  Candidato {i}: "
            f"{cromosoma_texto(individuo)} | "
            f"Aptitud = {calcular_aptitud(individuo):.2f}"
        )

    print("\nGanador del torneo:")

    mostrar_individuo(
        "PADRE 1",
        padre1
    )

    # --------------------------------------------------------
    # 3. SELECCIÓN DEL PADRE 2
    # --------------------------------------------------------

    padre2, torneo2 = seleccionar_padre(
        poblacion,
        tam_torneo=3
    )

    print("\nTorneo para seleccionar PADRE 2:")

    for i, individuo in enumerate(torneo2, start=1):

        print(
            f"  Candidato {i}: "
            f"{cromosoma_texto(individuo)} | "
            f"Aptitud = {calcular_aptitud(individuo):.2f}"
        )

    print("\nGanador del torneo:")

    mostrar_individuo(
        "PADRE 2",
        padre2
    )

    # --------------------------------------------------------
    # 4. CRUCE
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("2. CRUCE DE UN PUNTO")
    print("=" * 70)

    hijo1, hijo2, punto = cruzar(
        padre1,
        padre2
    )

    print(f"\nPunto de cruce: {punto}")

    print("\nPadres:")

    print(
        f"  PADRE 1: "
        f"{cromosoma_texto(padre1)}"
    )

    print(
        f"  PADRE 2: "
        f"{cromosoma_texto(padre2)}"
    )

    print("\nHijos antes de la mutación:")

    print(
        f"  HIJO 1: "
        f"{cromosoma_texto(hijo1)}"
    )

    print(
        f"  HIJO 2: "
        f"{cromosoma_texto(hijo2)}"
    )

    # --------------------------------------------------------
    # 5. MUTACIÓN
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("3. MUTACIÓN")
    print("=" * 70)

    hijo1_mutado, posiciones1 = mutar(
        hijo1,
        PROB_MUTACION
    )

    hijo2_mutado, posiciones2 = mutar(
        hijo2,
        PROB_MUTACION
    )

    print(f"\nProbabilidad de mutación: {PROB_MUTACION}")

    print("\nHIJO 1:")

    print(
        f"  Antes  : "
        f"{cromosoma_texto(hijo1)}"
    )

    if posiciones1:
        print(
            f"  Genes mutados: {posiciones1}"
        )
    else:
        print("  No hubo mutaciones.")

    print(
        f"  Después: "
        f"{cromosoma_texto(hijo1_mutado)}"
    )

    print("\nHIJO 2:")

    print(
        f"  Antes  : "
        f"{cromosoma_texto(hijo2)}"
    )

    if posiciones2:
        print(
            f"  Genes mutados: {posiciones2}"
        )
    else:
        print("  No hubo mutaciones.")

    print(
        f"  Después: "
        f"{cromosoma_texto(hijo2_mutado)}"
    )

    # --------------------------------------------------------
    # 6. RESULTADO FINAL
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("4. RESULTADO FINAL DE LOS HIJOS")
    print("=" * 70)

    print()

    mostrar_individuo(
        "HIJO 1 FINAL",
        hijo1_mutado
    )

    print()

    mostrar_individuo(
        "HIJO 2 FINAL",
        hijo2_mutado
    )

    print("\n" + "=" * 70)
    print("FIN DEL PUNTO 3")
    print("=" * 70)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":
    demostracion_punto3()

import random
import time
import csv
import matplotlib.pyplot as plt

from punto4.punto4 import (
    CONFIG,
    ejecutar_algoritmo_genetico,
    calcular_beneficio,
    calcular_costo,
    proyectos_seleccionados,
)


EXPERIMENTOS = {
    "A": {
        "tamano_poblacion": 10,
        "num_generaciones": 50,
        "prob_mutacion": 0.01,
    },
    "B": {
        "tamano_poblacion": 20,
        "num_generaciones": 100,
        "prob_mutacion": 0.05,
    },
    "C": {
        "tamano_poblacion": 50,
        "num_generaciones": 200,
        "prob_mutacion": 0.10,
    },
}


def ejecutar_una_corrida(configuracion):
    inicio = time.perf_counter()

    historial, mejor, mejor_aptitud, generacion_mejor, diversidad = (
        ejecutar_algoritmo_genetico(configuracion)
    )

    fin = time.perf_counter()

    tiempo_ejecucion = fin - inicio

    resultado = {
        "beneficio": calcular_beneficio(mejor),
        "costo": calcular_costo(mejor),
        "proyectos": proyectos_seleccionados(mejor),
        "generacion_mejor": generacion_mejor,
        "tiempo": tiempo_ejecucion,
        "aptitud_promedio_final": historial[-1][5],
        "mejor_aptitud": mejor_aptitud,
        "historial": historial,
        "diversidad": diversidad,
    }

    return resultado


def ejecutar_cinco_corridas_iniciales():
    print("\n" + "=" * 70)
    print("CINCO EJECUCIONES - CONFIGURACION INICIAL")
    print("=" * 70)

    resultados = []
    lineas = []

    for i in range(1, 6):
        resultado = ejecutar_una_corrida(CONFIG)
        resultados.append(resultado)

        print(f"\nCorrida {i}")
        print(f"Beneficio: {resultado['beneficio']}")
        print(f"Costo: {resultado['costo']}")
        print(f"Proyectos: {resultado['proyectos']}")
        print(f"Generacion mejor: {resultado['generacion_mejor']}")
        print(f"Tiempo: {resultado['tiempo']:.6f} segundos")
        print(
            f"Aptitud promedio final: "
            f"{resultado['aptitud_promedio_final']:.2f}"
        )

        lineas.append(f"Corrida {i}")
        lineas.append(f"Beneficio: {resultado['beneficio']}")
        lineas.append(f"Costo: {resultado['costo']}")
        lineas.append(f"Proyectos: {resultado['proyectos']}")
        lineas.append(
            f"Generacion mejor: {resultado['generacion_mejor']}"
        )
        lineas.append(
            f"Tiempo: {resultado['tiempo']:.6f} segundos"
        )
        lineas.append(
            f"Aptitud promedio final: "
            f"{resultado['aptitud_promedio_final']:.2f}"
        )
        lineas.append("")

    # Guardar resultados en TXT
    with open(
        "punto5/resultados/corridas_iniciales.txt",
        "w",
        encoding="utf-8"
    ) as archivo:
        archivo.write("\n".join(lineas))

    # Guardar resultados en CSV
    with open(
        "punto5/resultados/tabla_corridas_iniciales.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow([
            "Corrida",
            "Beneficio",
            "Costo",
            "Proyectos",
            "Generacion mejor",
            "Tiempo (s)",
            "Aptitud promedio final"
        ])

        for i, resultado in enumerate(resultados, start=1):
            escritor.writerow([
                i,
                resultado["beneficio"],
                resultado["costo"],
                ", ".join(resultado["proyectos"]),
                resultado["generacion_mejor"],
                f"{resultado['tiempo']:.6f}",
                f"{resultado['aptitud_promedio_final']:.2f}"
            ])

    return resultados


def ejecutar_experimentos():
    print("\n" + "=" * 70)
    print("EXPERIMENTOS A, B Y C")
    print("=" * 70)

    resultados = {}
    lineas = []

    for nombre, cambios in EXPERIMENTOS.items():

        configuracion = CONFIG.copy()
        configuracion.update(cambios)

        resultado = ejecutar_una_corrida(configuracion)
        resultados[nombre] = resultado

        print(f"\nExperimento {nombre}")
        print(
            f"Poblacion: "
            f"{configuracion['tamano_poblacion']}"
        )
        print(
            f"Generaciones: "
            f"{configuracion['num_generaciones']}"
        )
        print(
            f"Mutacion: "
            f"{configuracion['prob_mutacion']}"
        )
        print(f"Beneficio: {resultado['beneficio']}")
        print(f"Costo: {resultado['costo']}")
        print(f"Proyectos: {resultado['proyectos']}")
        print(
            f"Generacion mejor: "
            f"{resultado['generacion_mejor']}"
        )
        print(
            f"Tiempo: "
            f"{resultado['tiempo']:.6f} segundos"
        )
        print(
            f"Aptitud promedio final: "
            f"{resultado['aptitud_promedio_final']:.2f}"
        )

        lineas.append(f"Experimento {nombre}")
        lineas.append(
            f"Poblacion: "
            f"{configuracion['tamano_poblacion']}"
        )
        lineas.append(
            f"Generaciones: "
            f"{configuracion['num_generaciones']}"
        )
        lineas.append(
            f"Mutacion: "
            f"{configuracion['prob_mutacion']}"
        )
        lineas.append(f"Beneficio: {resultado['beneficio']}")
        lineas.append(f"Costo: {resultado['costo']}")
        lineas.append(f"Proyectos: {resultado['proyectos']}")
        lineas.append(
            f"Generacion mejor: "
            f"{resultado['generacion_mejor']}"
        )
        lineas.append(
            f"Tiempo: "
            f"{resultado['tiempo']:.6f} segundos"
        )
        lineas.append(
            f"Aptitud promedio final: "
            f"{resultado['aptitud_promedio_final']:.2f}"
        )
        lineas.append("")

    # Guardar resultados en TXT
    with open(
        "punto5/resultados/experimentos.txt",
        "w",
        encoding="utf-8"
    ) as archivo:
        archivo.write("\n".join(lineas))

    # Guardar resultados en CSV
    with open(
        "punto5/resultados/tabla_experimentos.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow([
            "Experimento",
            "Poblacion",
            "Generaciones",
            "Mutacion",
            "Beneficio",
            "Costo",
            "Proyectos",
            "Generacion mejor",
            "Tiempo (s)",
            "Aptitud promedio final"
        ])

        for nombre, cambios in EXPERIMENTOS.items():
            resultado = resultados[nombre]

            escritor.writerow([
                nombre,
                cambios["tamano_poblacion"],
                cambios["num_generaciones"],
                cambios["prob_mutacion"],
                resultado["beneficio"],
                resultado["costo"],
                ", ".join(resultado["proyectos"]),
                resultado["generacion_mejor"],
                f"{resultado['tiempo']:.6f}",
                f"{resultado['aptitud_promedio_final']:.2f}"
            ])

    return resultados


def graficar_resultado(nombre, resultado):
    generaciones = []
    mejores_aptitudes = []
    aptitudes_promedio = []

    for registro in resultado["historial"]:
        generaciones.append(registro[0])
        mejores_aptitudes.append(registro[1])
        aptitudes_promedio.append(registro[5])

    plt.figure()

    plt.plot(
        generaciones,
        mejores_aptitudes,
        label="Mejor aptitud"
    )

    plt.plot(
        generaciones,
        aptitudes_promedio,
        label="Aptitud promedio"
    )

    plt.title(
        f"Evolucion de aptitud - Experimento {nombre}"
    )
    plt.xlabel("Generacion")
    plt.ylabel("Aptitud")
    plt.legend()
    plt.grid()

    plt.savefig(
        f"punto5/graficas/experimento_{nombre}.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


def main():
    # 1. Cinco ejecuciones con la configuracion inicial
    ejecutar_cinco_corridas_iniciales()

    # 2. Experimentos A, B y C
    resultados_experimentos = ejecutar_experimentos()

    # 3. Graficas de cada experimento
    for nombre, resultado in resultados_experimentos.items():
        graficar_resultado(nombre, resultado)


if __name__ == "__main__":
    main()
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


NUM_CORRIDAS = 5


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
        "diversidad_final": diversidad[-1],
        "diversidad_promedio": sum(diversidad) / len(diversidad),
    }

    return resultado


def ejecutar_cinco_corridas_iniciales():
    print("\n" + "=" * 70)
    print("CINCO EJECUCIONES - CONFIGURACION INICIAL")
    print("=" * 70)

    resultados = []
    lineas = []

    for i in range(1, NUM_CORRIDAS + 1):
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

    with open(
        "punto5/resultados/corridas_iniciales.txt",
        "w",
        encoding="utf-8"
    ) as archivo:
        archivo.write("\n".join(lineas))

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
    print("EXPERIMENTOS A, B Y C - CINCO CORRIDAS CADA UNO")
    print("=" * 70)

    resultados_experimentos = {}
    lineas = []

    for nombre, cambios in EXPERIMENTOS.items():

        print("\n" + "-" * 70)
        print(f"EXPERIMENTO {nombre}")
        print("-" * 70)

        configuracion = CONFIG.copy()
        configuracion.update(cambios)

        corridas = []

        for numero_corrida in range(1, NUM_CORRIDAS + 1):

            resultado = ejecutar_una_corrida(configuracion)
            corridas.append(resultado)

            print(f"\nCorrida {numero_corrida}")
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
            print(
                f"Diversidad final: "
                f"{resultado['diversidad_final']}"
            )
            print(
                f"Diversidad promedio: "
                f"{resultado['diversidad_promedio']:.2f}"
            )

            lineas.append(
                f"Experimento {nombre} - Corrida {numero_corrida}"
            )
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
            lineas.append(
                f"Beneficio: {resultado['beneficio']}"
            )
            lineas.append(
                f"Costo: {resultado['costo']}"
            )
            lineas.append(
                f"Proyectos: {resultado['proyectos']}"
            )
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
            lineas.append(
                f"Diversidad final: "
                f"{resultado['diversidad_final']}"
            )
            lineas.append(
                f"Diversidad promedio: "
                f"{resultado['diversidad_promedio']:.2f}"
            )
            lineas.append("")

        resultados_experimentos[nombre] = {
            "configuracion": configuracion,
            "corridas": corridas,
        }

    with open(
        "punto5/resultados/experimentos.txt",
        "w",
        encoding="utf-8"
    ) as archivo:
        archivo.write("\n".join(lineas))

    guardar_tabla_detalle(resultados_experimentos)
    guardar_tabla_resumen(resultados_experimentos)

    return resultados_experimentos


def guardar_tabla_detalle(resultados_experimentos):

    with open(
        "punto5/resultados/tabla_experimentos_detalle.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([
            "Experimento",
            "Corrida",
            "Poblacion",
            "Generaciones",
            "Mutacion",
            "Beneficio",
            "Costo",
            "Proyectos",
            "Generacion mejor",
            "Tiempo (s)",
            "Aptitud promedio final",
            "Diversidad final",
            "Diversidad promedio"
        ])

        for nombre, datos in resultados_experimentos.items():

            configuracion = datos["configuracion"]

            for numero, resultado in enumerate(
                datos["corridas"],
                start=1
            ):

                escritor.writerow([
                    nombre,
                    numero,
                    configuracion["tamano_poblacion"],
                    configuracion["num_generaciones"],
                    configuracion["prob_mutacion"],
                    resultado["beneficio"],
                    resultado["costo"],
                    ", ".join(resultado["proyectos"]),
                    resultado["generacion_mejor"],
                    f"{resultado['tiempo']:.6f}",
                    f"{resultado['aptitud_promedio_final']:.2f}",
                    resultado["diversidad_final"],
                    f"{resultado['diversidad_promedio']:.2f}"
                ])


def guardar_tabla_resumen(resultados_experimentos):

    with open(
        "punto5/resultados/tabla_resumen_experimentos.csv",
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
            "Beneficio promedio",
            "Mejor beneficio",
            "Costo mejor solucion",
            "Proyectos mejor solucion",
            "Generacion promedio mejor",
            "Tiempo promedio (s)",
            "Aptitud promedio final",
            "Diversidad final promedio",
            "Diversidad promedio"
        ])

        for nombre, datos in resultados_experimentos.items():

            configuracion = datos["configuracion"]
            corridas = datos["corridas"]

            mejor_corrida = max(
                corridas,
                key=lambda resultado: resultado["mejor_aptitud"]
            )

            beneficio_promedio = (
                sum(
                    resultado["beneficio"]
                    for resultado in corridas
                )
                / len(corridas)
            )

            generacion_promedio = (
                sum(
                    resultado["generacion_mejor"]
                    for resultado in corridas
                )
                / len(corridas)
            )

            tiempo_promedio = (
                sum(
                    resultado["tiempo"]
                    for resultado in corridas
                )
                / len(corridas)
            )

            aptitud_final_promedio = (
                sum(
                    resultado["aptitud_promedio_final"]
                    for resultado in corridas
                )
                / len(corridas)
            )

            diversidad_final_promedio = (
                sum(
                    resultado["diversidad_final"]
                    for resultado in corridas
                )
                / len(corridas)
            )

            diversidad_promedio = (
                sum(
                    resultado["diversidad_promedio"]
                    for resultado in corridas
                )
                / len(corridas)
            )

            escritor.writerow([
                nombre,
                configuracion["tamano_poblacion"],
                configuracion["num_generaciones"],
                configuracion["prob_mutacion"],
                f"{beneficio_promedio:.2f}",
                mejor_corrida["beneficio"],
                mejor_corrida["costo"],
                ", ".join(mejor_corrida["proyectos"]),
                f"{generacion_promedio:.2f}",
                f"{tiempo_promedio:.6f}",
                f"{aptitud_final_promedio:.2f}",
                f"{diversidad_final_promedio:.2f}",
                f"{diversidad_promedio:.2f}"
            ])


def graficar_experimento(nombre, datos):

    corridas = datos["corridas"]

    cantidad_generaciones = len(
        corridas[0]["historial"]
    )

    generaciones = []
    mejores_aptitudes_promedio = []
    aptitudes_promedio = []

    for indice in range(cantidad_generaciones):

        generaciones.append(
            corridas[0]["historial"][indice][0]
        )

        mejor_promedio = (
            sum(
                corrida["historial"][indice][1]
                for corrida in corridas
            )
            / len(corridas)
        )

        aptitud_poblacion_promedio = (
            sum(
                corrida["historial"][indice][5]
                for corrida in corridas
            )
            / len(corridas)
        )

        mejores_aptitudes_promedio.append(
            mejor_promedio
        )

        aptitudes_promedio.append(
            aptitud_poblacion_promedio
        )

    plt.figure()

    plt.plot(
        generaciones,
        mejores_aptitudes_promedio,
        label="Mejor aptitud promedio"
    )

    plt.plot(
        generaciones,
        aptitudes_promedio,
        label="Aptitud promedio de la poblacion"
    )

    plt.title(
        f"Evolucion promedio de aptitud - Experimento {nombre}"
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

    # 2. Cinco ejecuciones para cada experimento A, B y C
    resultados_experimentos = ejecutar_experimentos()

    # 3. Graficas promedio de los cinco ensayos
    for nombre, datos in resultados_experimentos.items():
        graficar_experimento(nombre, datos)


if __name__ == "__main__":
    main()
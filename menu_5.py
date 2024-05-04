# Simulación de días en el sistema de gestión de agua

import variables  # Asumimos que las variables contienen la estructura necesaria para la simulación


def calcular_eficiencia(fuente_calidad, planta_eficiencia):
    penalizacion = 0
    if fuente_calidad != "Potable" and fuente_calidad != "No Potabilizable":
        if planta_eficiencia == "Alta":
            penalizacion += variables.calidad_del_agua_indice[fuente_calidad]
        elif planta_eficiencia == "Media":
            penalizacion += 0.1  # Ejemplo de penalización
        elif planta_eficiencia == "Baja":
            penalizacion += 0.2
    return max(0, 1 - penalizacion)  # Asegura que la eficiencia no sea negativa


def simular_dia():
    print("Fase 1: Fuentes a Plantas")
    # 1) Fuentes entregan agua a las plantas potabilizadoras
    for interconexion in variables.interconexiones_fh:
        fuente = next(
            (f for f in variables.fuentes_hidricas_usuarios
            if f["Id"] == interconexion["Origen"]
            ),
            None,
        )
        planta = next(
            (
                p
                for p in variables.plantas_potabilizadoras_usuarios
                if p["Id"] == interconexion["Porcentaje"]
            ),
            None,
        )
        if fuente and planta:
            eficiencia = calcular_eficiencia(fuente["Calidad"], planta["Eficiencia"])
            agua_entregada = (
                fuente["Litros"] * interconexion["Porcentaje"] / 100 * eficiencia
            )
            planta["Litros"] = planta.get("Litros", 0) + agua_entregada

    print("Fase 2: Plantas potabilizan y entregan agua")
    # 2 y 3) Plantas potabilizan agua y la entregan a centros
    for interconexion in variables.interconexiones_pb:
        planta = next(
            (
                p
                for p in variables.plantas_potabilizadoras_usuarios
                if p["Id"] == interconexion["Origen"]
            ),
            None,
        )
        centro = next(
            (
                c
                for c in variables.centros_distribucion_usuarios
                if c["Id"] == interconexion["Destino"]
            ),
            None,
        )
        if planta and centro:
            agua_potabilizada = planta.get("Litros", 0)
            agua_entregada = agua_potabilizada * interconexion["Porcentaje"] / 100
            centro["Reserva temporal"] = (
                centro.get("Reserva temporal", 0) + agua_entregada
            )

    print("Fase 4: Consumo en centros")
    # 4) Centros de distribución consumen agua
    for centro in variables.centros_distribucion_usuarios:
        centro["Reserva temporal"] -= centro["Consumo diario"]

    print("Fase 5: Corrección de desbordes")
    # 5) Cierre día: Corrección de desbordes temporales
    for centro in variables.centros_distribucion_usuarios:
        if centro["Reserva temporal"] > centro["Capacidad máxima"]:
            centro["Reserva temporal"] = centro["Capacidad máxima"]
        centro["Reserva actual"] = centro["Reserva temporal"]


def menu_dias():
    dias = int(input("Introduce la cantidad de días para la simulación: "))
    while dias <= 0:
        print("Por favor, introduce un número entero positivo mayor que cero.")
        dias = int(input("Introduce la cantidad de días para la simulación: "))

    for dia in range(dias):
        print(f"Simulando día {dia + 1}...")
        simular_dia()
        print("Simulación completada para el día.")

    print("Simulación finalizada. Volviendo al menú principal.")


# Incluimos esta sección para permitir ejecución directa
if __name__ == "__main__":
    menu_dias()

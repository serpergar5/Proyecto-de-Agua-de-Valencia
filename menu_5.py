import variables
import menu_principal


def calcular_eficiencia(fuente_calidad):
    penalizacion = 0
    if fuente_calidad != "Potable" and fuente_calidad != "No Potabilizable":
        penalizacion += variables.calidad_del_agua_indice[fuente_calidad]

    return penalizacion


def simular_dia():
    print("Fase 1: Fuentes a Plantas")
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
                if p["Id"] == interconexion["Destino"]
            ),
            None,
        )
        if fuente and planta:
            eficiencia = calcular_eficiencia(fuente["Calidad"])
            agua_entregada_fhpb = (
                fuente["Litros"] * interconexion["Porcentaje"] / 100 * eficiencia
            )
            planta["Litros"] = planta.get("Litros", 0) + agua_entregada_fhpb

    print("Fase 2 y 3: Plantas potabilizan y entregan agua")
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
            agua_entregada_pbcd = agua_potabilizada * interconexion["Porcentaje"] / 100
            centro["Reserva temporal"] = (
                centro.get("Reserva temporal", 0) + agua_entregada_pbcd
            )

    print("Fase 4: Consumo en centros")
    for centro in variables.centros_distribucion_usuarios:
        centro["Reserva temporal"] -= centro["Consumo diario"]

    print("Fase 5: Corrección de desbordes")
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
    menu_principal.menu_principal

if __name__ == "__main__":
    menu_dias()

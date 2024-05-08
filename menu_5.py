import variables
import menu_principal


def simular_dia():
    try:
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
                calidad = variables.calidad_del_agua_indice[fuente["Calidad"]]
                agua_entregada_fhpb = (
                    float(fuente["Litros"]) * float(interconexion["Porcentaje"]) / 100 * calidad
                )
                planta["Litros"] = float(planta["Litros"]) + agua_entregada_fhpb

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
                agua_potabilizada = float(planta["Litros"])
                eficiencia = variables.eficiencia_de_la_planta_indice[planta["Eficiencia"]]
                agua_entregada_pbcd = agua_potabilizada * float(interconexion["Porcentaje"]) / 100 * eficiencia
                centro["Reserva actual"] = float(centro["Reserva actual"]) + agua_entregada_pbcd
                if centro["Reserva actual"] > float(centro["Capacidad máxima"]):
                    reserva_temporal = float(centro["Reserva actual"]) - float(centro["Capacidad máxima"])
                    centro["Reserva temporal"] = float(reserva_temporal)
            
        print("Fase 4: Consumo en centros")
        for centro in variables.centros_distribucion_usuarios:
            if (float(centro["Reserva actual"]) - float(centro["Consumo diario"])) > 0:
                centro["Reserva actual"] = float(centro["Reserva actual"]) - float(centro["Consumo diario"])
            else:
                centro["Reserva actual"] = 0
                print(f"El centro {centro['Id']} se ha quedado sin agua.")
        print("Fase 5: Corrección de desbordes")
        for centro in variables.centros_distribucion_usuarios:
            if "Reserva temporal" in centro and (centro["Reserva temporal"] + centro["Reserva actual"]) <= float(centro["Capacidad máxima"]):
                centro["Reserva actual"] = centro["Reserva actual"] + centro["Reserva temporal"]
                del centro["Reserva temporal"]
            elif "Reserva temporal" in centro and (centro["Reserva temporal"] + centro["Reserva actual"]) > float(centro["Capacidad máxima"]):
                centro["Reserva actual"] = centro["Capacidad máxima"]
                del centro["Reserva temporal"]
    except:
        print("Error al simular el día.")
        menu_principal.menu_principal()


def menu_dias():
    try:
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
    except:
        print("Error al simular los días.")
        menu_principal.menu_principal()

if __name__ == "__main__":
    menu_dias()

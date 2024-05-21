import variables
import menu_principal

# Simula un día en el sistema
def simular_dia():
    try:
        # Fase 1: Fuentes a Plantas
        print("Fase 1: Fuentes a Plantas")
        # Iteramos sobre las interconexiones de fuentes a plantas
        for interconexion in variables.interconexiones_fh:
            fuente = next((f for f in variables.fuentes_hidricas_usuarios if f["Id"] == interconexion["Origen"]),None)
            # Buscamos la planta potabilizadora correspondiente a la interconexión actual en la lista de plantas potabilizadoras de los usuarios
            planta = next((p for p in variables.plantas_potabilizadoras_usuarios if p["Id"] == interconexion["Destino"]),None)
            # Si encontramos la fuente y la planta potabilizadora correspondientes, calculamos la cantidad de agua entregada
            if fuente and planta:
                # Calculamos la calidad del agua de la fuente actual
                calidad = variables.calidad_del_agua_indice[fuente["Calidad"]]
                # Calculamos la cantidad de agua entregada a la planta potabilizadora actual
                agua_entregada_fhpb = (
                    float(fuente["Litros"]) * float(interconexion["Porcentaje"]) / 100 * calidad
                )
                # Añadimos la cantidad de agua entregada a la planta potabilizadora actual 
                planta["Litros"] = float(planta["Litros"]) + agua_entregada_fhpb
                
        # Fase 2 y 3: Plantas a Centros
        print("Fase 2 y 3: Plantas potabilizan y entregan agua")
        # Iteramos sobre las interconexiones de plantas a centros
        for interconexion in variables.interconexiones_pb:
            # Buscamos la planta potabilizadora correspondiente a la interconexión actual en la lista de plantas potabilizadoras de los usuarios
            planta = next(
                (
                    p
                    for p in variables.plantas_potabilizadoras_usuarios
                    if p["Id"] == interconexion["Origen"]
                ),
                None,
            )
            # Buscamos el centro de distribución correspondiente a la interconexión actual en la lista de centros de distribución de los usuarios
            centro = next(
                (
                    c
                    for c in variables.centros_distribucion_usuarios
                    if c["Id"] == interconexion["Destino"]
                ),
                None,
            )
            # Si encontramos la planta y el centro correspondientes, calculamos la cantidad de agua potabilizada y entregada
            if planta and centro:
                # Calculamos la cantidad de agua potabilizada por la planta actual y la eficiencia de la planta actual
                agua_potabilizada = float(planta["Litros"])
                eficiencia = variables.eficiencia_de_la_planta_indice[planta["Eficiencia"]]
                agua_entregada_pbcd = agua_potabilizada * float(interconexion["Porcentaje"]) / 100 * eficiencia
                centro["Reserva actual"] = float(centro["Reserva actual"]) + agua_entregada_pbcd
                if centro["Reserva actual"] > float(centro["Capacidad máxima"]):
                    reserva_temporal = float(centro["Reserva actual"]) - float(centro["Capacidad máxima"])
                    centro["Reserva temporal"] = float(reserva_temporal)
        # Fase 4: Consumo en centros
        print("Fase 4: Consumo en centros")
        # Iteramos sobre los centros de distribución de los usuarios y calculamos el consumo diario de agua
        for centro in variables.centros_distribucion_usuarios:
            # Calculamos el consumo diario de agua del centro actual
            if (float(centro["Reserva actual"]) - float(centro["Consumo diario"])) > 0:
                centro["Reserva actual"] = float(centro["Reserva actual"]) - float(centro["Consumo diario"])
            # Si el consumo diario de agua es mayor que la reserva actual del centro, el centro se queda sin agua
            else:
                centro["Reserva actual"] = 0
                print(f"El centro {centro['Id']} se ha quedado sin agua.")
                
        # Fase 5: Corrección de desbordes
        print("Fase 5: Corrección de desbordes")
        # Iteramos sobre los centros de distribución de los usuarios y corregimos los desbordes
        for centro in variables.centros_distribucion_usuarios:
            # Si la reserva temporal del centro actual es mayor que 0, corregimos el desborde y eliminamos la reserva temporal
            if "Reserva temporal" in centro and (centro["Reserva temporal"] + centro["Reserva actual"]) <= float(centro["Capacidad máxima"]):
                centro["Reserva actual"] = centro["Reserva actual"] + centro["Reserva temporal"]
                del centro["Reserva temporal"]
            # Si la reserva temporal del centro actual es mayor que 0 y la suma de la reserva temporal y la reserva actual es mayor que la capacidad máxima del centro, corregimos el desborde y establecemos la reserva actual al máximo
            elif "Reserva temporal" in centro and (centro["Reserva temporal"] + centro["Reserva actual"]) > float(centro["Capacidad máxima"]):
                centro["Reserva actual"] = centro["Capacidad máxima"]
                del centro["Reserva temporal"]
    except:
        print("Error al simular el día.")
        menu_principal.menu_principal()

# Menú de simulación de días
def menu_dias():
    try:
        # Solicitamos al usuario la cantidad de días a simular y validamos la entrada del usuario para asegurarnos de que sea un número entero positivo mayor que cero
        dias = int(input("Introduce la cantidad de días para la simulación: "))
        while dias <= 0:
            print("Por favor, introduce un número entero positivo mayor que cero.")
            dias = int(input("Introduce la cantidad de días para la simulación: "))
        
        # Simulamos los días solicitados por el usuario y mostramos un mensaje de confirmación al finalizar la simulación
        for dia in range(dias):
            print(f"Simulando día {dia + 1}...")
            simular_dia()
            print("Simulación completada para el día " + str(dia +1))
        print("Simulación finalizada. Volviendo al menú principal.")
        menu_principal.menu_principal
        
    except:
        print("Error al simular los días.")
        menu_principal.menu_principal()

if __name__ == "__main__":
    menu_dias()

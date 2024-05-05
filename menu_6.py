# Info Sistema para el sistema de gestión de agua

import variables  # Asumimos que las variables contienen la estructura necesaria para la información

def mostrar_info_fuentes():
    print("\nFuentes Hídricas:")
    for fuente in variables.fuentes_hidricas_usuarios:
        print("ID: " + fuente['Id'] + ", Calidad del agua: " + fuente['calidad'] + ", Litros por día: " + str(fuente['litros']))

def mostrar_info_plantas():
    print("\nPlantas Potabilizadoras:")
    for planta in variables.plantas_potabilizadoras_usuarios:
        print("ID: " + planta['Id'] + ", Eficiencia: " + planta['eficiencia'] + ", Agua potabilizada: " + str(planta.get('agua_potabilizada', 'No disponible')))

def mostrar_info_centros():
    print("\nCentros de Distribución:")
    for centro in variables.centros_distribucion_usuarios:
        print("ID: " + centro['Id'] + ", Capacidad máxima: " + str(centro['capacidad_reserva']) + ", Reserva actual: " + str(centro.get('reserva_actual', 'No disponible')))

def mostrar_info_interconexiones():
    print("\nInterconexiones:")
    print("Fuentes a Plantas:")
    for inter in variables.interconexiones_fh:
        print("Origen: " + inter['origen'] + " -> Destino: " + inter['destino'] + ", Capacidad: " + str(inter['capacidad']) + "%")
    print("Plantas a Centros:")
    for inter in variables.interconexiones_pb:
        print("Origen: " + inter['origen'] + " -> Destino: " + inter['destino'] + ", Capacidad: " + str(inter['capacidad']) + "%")

def menu_info_sistema():
    mostrar_info_fuentes()
    mostrar_info_plantas()
    mostrar_info_centros()
    mostrar_info_interconexiones()

    print("\nInformación completa del sistema mostrada. Volviendo al menú principal.")

# Incluimos esta sección para permitir ejecución directa
if __name__ == "__main__":
    menu_info_sistema()

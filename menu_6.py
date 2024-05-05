import menu_principal
import variables

def mostrar_info_fuentes():
    print("\nFuentes Hídricas:")
    for fuente in variables.fuentes_hidricas_usuarios:
        print("ID: " + fuente['Id'] + ", Calidad del agua: " + fuente['Calidad'] + ", Litros: " + str(fuente['Litros']))

def mostrar_info_plantas():
    print("\nPlantas Potabilizadoras:")
    for planta in variables.plantas_potabilizadoras_usuarios:
        print("ID: " + planta['Id'] + ", Eficiencia: " + planta['Eficiencia'] + ", Litros: " + str(planta.get('Litros', 'No disponible')))

def mostrar_info_centros():
    print("\nCentros de Distribución:")
    for centro in variables.centros_distribucion_usuarios:
        print("ID: " + centro['Id'] + ", Capacidad máxima: " + str(centro['Capacidad máxima']) + ", Reserva actual: " + str(centro.get('Reserva actual', 'No disponible')))

def mostrar_info_interconexiones():
    print("\nInterconexiones:")
    print("Fuentes a Plantas:")
    for inter in variables.interconexiones_fh:
        print("Origen: " + inter['Origen'] + " -> Destino: " + inter['Destino'] + ", Porcentaje: " + str(inter['Porcentaje']) + "%")
    print("Plantas a Centros:")
    for inter in variables.interconexiones_pb:
        print("Origen: " + inter['Origen'] + " -> Destino: " + inter['Destino'] + ", Porcentaje: " + str(inter['Porcentaje']) + "%")

def menu_info_sistema():
    mostrar_info_fuentes()
    mostrar_info_plantas()
    mostrar_info_centros()
    mostrar_info_interconexiones()

    print("\nInformación completa del sistema mostrada. Volviendo al menú principal.")

# Incluimos esta sección para permitir ejecución directa
if __name__ == "__main__":
    menu_info_sistema()
    menu_principal.menu_principal()

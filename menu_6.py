import menu_principal
import variables

# Muestra la información de las fuentes hídricas
def mostrar_info_fuentes():
    try:
        print("\nFuentes Hídricas:")
        for fuente in variables.fuentes_hidricas_usuarios:
            print("ID: " + fuente['Id'] + ", Calidad del agua: " + fuente['Calidad'] + ", Litros: " + str(fuente['Litros']))
    except:
        print("Error al mostrar la información de las fuentes hídricas.")
        return

# Muestra la información de las plantas potabilizadoras
def mostrar_info_plantas():
    try:
        print("\nPlantas Potabilizadoras:")
        for planta in variables.plantas_potabilizadoras_usuarios:
            print("ID: " + planta['Id'] + ", Eficiencia: " + planta['Eficiencia'] + ", Litros: " + str(planta.get('Litros', 'No disponible')))
    except:
        print("Error al mostrar la información de las plantas potabilizadoras.")
        return
        
# Muestra la información de los centros de distribución
def mostrar_info_centros():
    try:
        print("\nCentros de Distribución:")
        for centro in variables.centros_distribucion_usuarios:
            print("ID: " + centro['Id'] + ", Capacidad máxima: " + str(centro['Capacidad máxima']) + ", Reserva actual: " + str(centro['Reserva actual']) + ", Consumo diario: " + str(centro['Consumo diario']))
    except:
        print("Error al mostrar la información de los centros de distribución.")
        return

# Muestra la información de las interconexiones
def mostrar_info_interconexiones():
    try:
        print("\nInterconexiones:")
        print("Fuentes a Plantas:")
        for inter in variables.interconexiones_fh:
            print("Origen: " + inter['Origen'] + " -> Destino: " + inter['Destino'] + ", Porcentaje: " + str(inter['Porcentaje']) + "%")
        print("Plantas a Centros:")
        for inter in variables.interconexiones_pb:
            print("Origen: " + inter['Origen'] + " -> Destino: " + inter['Destino'] + ", Porcentaje: " + str(inter['Porcentaje']) + "%")
    except:
        print("Error al mostrar la información de las interconexiones.")
        return

# Menú de información del sistema (fuentes, plantas, centros e interconexiones)
def menu_info_sistema():
    try:
        mostrar_info_fuentes()
        mostrar_info_plantas()
        mostrar_info_centros()
        mostrar_info_interconexiones()

        print("\nInformación completa del sistema mostrada. Volviendo al menú principal.")
    except:
        print("Error al mostrar la información del sistema.")
        return

# Incluimos esta sección para permitir ejecución directa
if __name__ == "__main__":
    menu_principal.menu()

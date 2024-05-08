import variables
import menu_principal

def mostrar_interconexiones(interconexiones):
    try:
        if interconexiones:
            print("\nListado de interconexiones existentes:")

            capacidad_usada_por_origen = {}
            for interc in interconexiones:
                if interc['origen'] not in capacidad_usada_por_origen:
                    capacidad_usada_por_origen[interc['origen']] = 0
                capacidad_usada_por_origen[interc['origen']] += interc['porcentaje']
            
            for interc in interconexiones:
                if capacidad_usada_por_origen[interc['origen']] < 100:
                    print(interc['Id'] + ": " + interc['origen'] + " a " + interc['destino'] + " - " + str(interc['porcentaje']) + "%")
        else:
            print("No hay interconexiones registradas.")
            return False
        return True
    except:
        print("Error al mostrar las interconexiones.")
        menu_principal.menu_principal()


def seleccionar_interconexion(interconexiones):
    try:
        if mostrar_interconexiones(interconexiones):
            id_interconexion = input(
                "Introduce el identificador de la interconexión a modificar o eliminar: "
            ).upper()
            return next(
                (interc for interc in interconexiones if interc["id"] == id_interconexion),
                None,
            )
        return None
    except:
        print("Error al seleccionar la interconexión.")
        menu_principal.menu_principal()


def modificar_interconexion(interc):
    try:
        nueva_capacidad = int(
            input("Introduce el nuevo porcentaje de la interconexión (1-100): ")
        )
        while nueva_capacidad <= 0 or nueva_capacidad > 100:
            print("Porcentaje inválido. Introduce un valor entre 1 y 100.")
            nueva_capacidad = int(
                input("Introduce el nuevo porcentaje de la interconexión (1-100): ")
            )
        interc["porcentaje"] = nueva_capacidad
        print("Interconexión actualizada con éxito.")
    except:
        print("Error al modificar la interconexión.")
        menu_principal.menu_principal()


def eliminar_interconexion(interconexiones, interc):
    try:
        interconexiones.remove(interc)
        print("Interconexión eliminada con éxito.")
    except:
        print("Error al eliminar la interconexión.")
        menu_principal.menu_principal()


def mostrar_recursos_disponibles(recursos):
    try:
        if recursos:
            print("\nListado de recursos disponibles para interconexión:")
            for i, recurso in enumerate(recursos):
                if i < len(recursos) - 1:
                    print(recurso['Id'], end=', ')
                else:
                    print(recurso['Id'])
        else:
            print("No hay recursos disponibles para interconexión. Asegúrate de haber añadido recursos antes de intentar interconectarlos.")
            return False
        return True
    except:
        print("Error al mostrar los recursos disponibles.")
        menu_principal.menu_principal()

def seleccionar_recurso(mensaje, recursos):
    try:
        print(mensaje)

        if recursos:
            ids_disponibles = ", ".join(recurso["Id"] for recurso in recursos)
            print("Recursos disponibles: " + ids_disponibles)
        else:
            print("No hay recursos disponibles.")
            return None

        while True:
            id_recurso = input("Introduce el identificador del recurso: ").upper()
            if any(recurso["Id"] == id_recurso for recurso in recursos):
                return id_recurso
            print("Identificador no válido. Intente de nuevo.")
    except:
        print("Error al seleccionar el recurso.")
        menu_principal.menu_principal()


def validar_capacidad_interconexion(id_origen, id_destino, porcentaje, interconexiones):
    try:
        uso_actual = sum(
            interc['porcentaje'] for interc in interconexiones
            if interc['origen'] == id_origen and interc['destino'] == id_destino
        )
        capacidad_disponible = 100 - uso_actual
        if porcentaje > capacidad_disponible:
            while porcentaje > capacidad_disponible:
                print("El porcentaje total de interconexión excede el 100%. Solo puedes asignar hasta un " + str(capacidad_disponible) + "% adicional.")
                porcentaje = int(input("Introduce un porcentaje igual o menor a " + str(capacidad_disponible) + "%: "))
        return porcentaje
    except:
        print("Error al validar la capacidad de la interconexión.")
        menu_principal.menu_principal()

def agregar_interconexion(id_origen, id_destino, porcentaje, interconexiones, tipo):
    try:
        nuevo_id = id_origen + "-" + id_destino + "-" + str(len(interconexiones) + 1)
        if tipo == "FH":
            variables.interconexiones_fh.append({
                "Id": nuevo_id,
                "Origen": id_origen,
                "Destino": id_destino,
                "Porcentaje": porcentaje,
            })
        else:
            variables.interconexiones_pb.append({
                "Id": nuevo_id,
                "Origen": id_origen,
                "Destino": id_destino,
                "Porcentaje": porcentaje,
            }) 
        print("Interconexión " + nuevo_id + " agregada con éxito.")
    except:
        print("Error al agregar la interconexión.")
        menu_principal.menu_principal()

def menu_interconexion():
    try:
        while True:
            tipo = input(
                "¿Deseas interconectar una Fuente Hídrica (FH) o una Planta Potabilizadora (PB)? "
            ).upper()
            while tipo not in ["FH", "PB"]:
                print(
                    "Opción inválida. Introduce 'FH' para Fuente Hídrica o 'PB' para Planta Potabilizadora."
                )
                tipo = input().upper()

            if tipo == "FH":
                recursos = variables.fuentes_hidricas_usuarios
                recursos_destino = variables.plantas_potabilizadoras_usuarios
                interconexiones_actuales = variables.interconexiones_fh
            elif tipo == "PB":
                recursos = variables.plantas_potabilizadoras_usuarios
                recursos_destino = variables.centros_distribucion_usuarios
                interconexiones_actuales = variables.interconexiones_pb

            if not mostrar_recursos_disponibles(recursos):
                print("Primero tienes que añadir datos antes de interconectarlos.")
                return

            if tipo == "FH" and variables.interconexiones_fh == []:
                accion = "Crear"
            elif tipo == "PB" and variables.interconexiones_pb == []:
                accion = "Crear"
            else:
                accion = input(
                    "¿Deseas crear una nueva interconexión, editar o eliminar una existente? (Crear/Editar/Eliminar): "
                ).capitalize()


            if accion == "Crear":
                origen = seleccionar_recurso("Selecciona el recurso de origen", recursos)
                destino = seleccionar_recurso("Selecciona el recurso de destino", recursos_destino)
                if any(interc['origen'] == origen and interc['destino'] == destino for interc in interconexiones_actuales):
                    print("Ya has introducido esto. Por favor, elige diferentes recursos o edita la interconexión existente.")
                    menu_interconexion()
                
                porcentaje = int(
                    input("Introduce el porcentaje de la interconexión (1-100): ")
                )
                while porcentaje <= 0 or porcentaje > 100:
                    print("Porcentaje inválido. Introduce un valor entre 1 y 100.")
                    porcentaje = int(
                        input("Introduce el porcentaje de la interconexión (1-100): ")
                    )
                capacidad_validada = validar_capacidad_interconexion(
                    origen, destino, porcentaje, interconexiones_actuales
                )
                agregar_interconexion(
                    origen, destino, capacidad_validada, interconexiones_actuales, tipo
                )
            elif accion == "Editar" or accion == "Eliminar":
                if mostrar_interconexiones(interconexiones_actuales):
                    interconexion = seleccionar_interconexion(interconexiones_actuales)
                    if interconexion:
                        if accion == "editar":
                            modificar_interconexion(interconexion, interconexiones_actuales)
                        elif accion == "eliminar":
                            eliminar_interconexion(interconexion, interconexiones_actuales)
                else:
                    print("No hay interconexiones existentes para modificar o eliminar.")
            if (
                input("¿Quieres continuar gestionando interconexiones? (sí/no): ").lower()
                != "sí"
            ):
                break
    except:
        print("Error al gestionar las interconexiones.")
        menu_principal.menu_principal()

if __name__ == "__main__":
    menu_interconexion()
    menu_principal.menu_principal()

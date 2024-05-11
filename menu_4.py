import variables
import menu_principal

# Muestra las interconexiones existentes
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

# Selecciona una interconexión existente
def seleccionar_interconexion(interconexiones):
    try:
        # Si hay interconexiones, se muestran y se solicita el identificador de la interconexión a modificar o eliminar
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

# Modifica una interconexión existente
def modificar_interconexion(interc):
    try:
        # Se solicita el nuevo porcentaje de la interconexión
        nueva_capacidad = int(
            input("Introduce el nuevo porcentaje de la interconexión (1-100): ")
        )
        # Se valida que el porcentaje sea válido (entre 1 y 100) y se actualiza la interconexión si es correcto
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

# Elimina una interconexión existente de la lista de interconexiones
def eliminar_interconexion(interconexiones, interc):
    try:
        interconexiones.remove(interc)
        print("Interconexión eliminada con éxito.")
    except:
        print("Error al eliminar la interconexión.")
        menu_principal.menu_principal()

# Muestra los recursos disponibles para interconectar (fuentes hídricas o plantas potabilizadoras)
def mostrar_recursos_disponibles(recursos):
    try:
        # Si hay recursos, se muestran y se solicita el identificador del recurso de origen y destino
        if recursos:
            print("\nListado de recursos disponibles para interconexión:")
            for i, recurso in enumerate(recursos):
                if i < len(recursos) - 1:
                    print(recurso['Id'], end=', ')
                else:
                    print(recurso['Id'])
        # Si no hay recursos, se muestra un mensaje de error
        else:
            print("No hay recursos disponibles para interconexión. Asegúrate de haber añadido recursos antes de intentar interconectarlos.")
            return False
        return True
    except:
        print("Error al mostrar los recursos disponibles.")
        menu_principal.menu_principal()

# Solicita al usuario que seleccione un recurso de origen o destino para la interconexión
def seleccionar_recurso(mensaje, recursos):
    try:
        # Se muestra el mensaje de selección y se solicita el identificador del recurso de origen o destino para la interconexión 
        print(mensaje)
        if recursos:
            ids_disponibles = ", ".join(recurso["Id"] for recurso in recursos)
            print("Recursos disponibles: " + ids_disponibles)
        # Si no hay recursos disponibles, se muestra un mensaje de error
        else:
            print("No hay recursos disponibles.")
            return None
        # Se valida que el identificador introducido sea válido y se devuelve el identificador del recurso seleccionado
        while True:
            id_recurso = input("Introduce el identificador del recurso: ").upper()
            if any(recurso["Id"] == id_recurso for recurso in recursos):
                return id_recurso
            # Si el identificador no es válido, se muestra un mensaje de error
            print("Identificador no válido. Intente de nuevo.")
    except:
        print("Error al seleccionar el recurso.")
        menu_principal.menu_principal()

# Valida que el porcentaje de interconexión no exceda el 100% y solicita un nuevo porcentaje si es necesario
def validar_capacidad_interconexion(id_origen, id_destino, porcentaje, interconexiones):
    try:
        # Se calcula el uso actual de la interconexión y la capacidad disponible
        uso_actual = sum(
            interc['porcentaje'] for interc in interconexiones
            if interc['origen'] == id_origen and interc['destino'] == id_destino
        )
        # Si el porcentaje total de interconexión excede el 100%, se solicita un nuevo porcentaje
        capacidad_disponible = 100 - uso_actual
        if porcentaje > capacidad_disponible:
            while porcentaje > capacidad_disponible:
                print("El porcentaje total de interconexión excede el 100%. Solo puedes asignar hasta un " + str(capacidad_disponible) + "% adicional.")
                porcentaje = int(input("Introduce un porcentaje igual o menor a " + str(capacidad_disponible) + "%: "))
        return porcentaje
    except:
        print("Error al validar la capacidad de la interconexión.")
        menu_principal.menu_principal()

# Agrega una nueva interconexión a la lista de interconexiones
def agregar_interconexion(id_origen, id_destino, porcentaje, interconexiones, tipo):
    try:
        # Se genera un nuevo identificador para la interconexión y se añade a la lista de interconexiones
        #TODO: Revisar el numero de ID
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

# Menú de gestión de interconexiones (crear, editar o eliminar)
def menu_interconexion():
    try:
        while True:
            # Se solicita al usuario que seleccione el tipo de recurso a interconectar (fuentes hídricas o plantas potabilizadoras)
            tipo = input(
                "¿Deseas interconectar una Fuente Hídrica (FH) o una Planta Potabilizadora (PB)? "
            ).upper()
            # Se valida que el tipo introducido sea válido
            while tipo not in ["FH", "PB"]:
                print(
                    "Opción inválida. Introduce 'FH' para Fuente Hídrica o 'PB' para Planta Potabilizadora."
                )
                tipo = input().upper()
            # Se seleccionan los recursos de origen y destino para la interconexión y se añaden a la lista de interconexiones correspondiente (fuentes hídricas)
            if tipo == "FH":
                recursos = variables.fuentes_hidricas_usuarios
                recursos_destino = variables.plantas_potabilizadoras_usuarios
                interconexiones_actuales = variables.interconexiones_fh
            # Se seleccionan los recursos de origen y destino para la interconexión y se añaden a la lista de interconexiones correspondiente (plantas potabilizadoras)
            elif tipo == "PB":
                recursos = variables.plantas_potabilizadoras_usuarios
                recursos_destino = variables.centros_distribucion_usuarios
                interconexiones_actuales = variables.interconexiones_pb
            # Se muestran los recursos disponibles para interconectar y se solicita al usuario que seleccione un recurso de origen y destino
            if not mostrar_recursos_disponibles(recursos):
                print("Primero tienes que añadir datos antes de interconectarlos.")
                return
            # Se solicita al usuario que seleccione una acción a realizar (crear, editar o eliminar una interconexión) o se crea una nueva interconexión si no hay interconexiones existentes
            if tipo == "FH" and variables.interconexiones_fh == []:
                accion = "Crear"
            elif tipo == "PB" and variables.interconexiones_pb == []:
                accion = "Crear"
            else:
                accion = input(
                    "¿Deseas crear una nueva interconexión, editar o eliminar una existente? (Crear/Editar/Eliminar): "
                ).capitalize()

            # Se ejecuta la acción seleccionada por el usuario
            if accion == "Crear":
                origen = seleccionar_recurso("Selecciona el recurso de origen", recursos)
                destino = seleccionar_recurso("Selecciona el recurso de destino", recursos_destino)
                if any(interc['origen'] == origen and interc['destino'] == destino for interc in interconexiones_actuales):
                    print("Ya has introducido esto. Por favor, elige diferentes recursos o edita la interconexión existente.")
                    menu_interconexion()
                # Se solicita al usuario que introduzca el porcentaje de interconexión y se valida que sea correcto
                porcentaje = int(
                    input("Introduce el porcentaje de la interconexión (1-100): ")
                )
                # Se valida que el porcentaje sea válido (entre 1 y 100) y se añade la interconexión a la lista de interconexiones si es correcto
                while porcentaje <= 0 or porcentaje > 100:
                    print("Porcentaje inválido. Introduce un valor entre 1 y 100.")
                    porcentaje = int(
                        input("Introduce el porcentaje de la interconexión (1-100): ")
                    )
                # Se valida que el porcentaje de interconexión no exceda el 100% y se solicita un nuevo porcentaje si es necesario
                capacidad_validada = validar_capacidad_interconexion(
                    origen, destino, porcentaje, interconexiones_actuales
                )
                # Se añade la interconexión a la lista de interconexiones
                agregar_interconexion(
                    origen, destino, capacidad_validada, interconexiones_actuales, tipo
                )
            # Se edita o elimina una interconexión existente
            elif accion == "Editar" or accion == "Eliminar":
                if mostrar_interconexiones(interconexiones_actuales):
                    interconexion = seleccionar_interconexion(interconexiones_actuales)
                    if interconexion:
                        if accion == "editar":
                            modificar_interconexion(interconexion, interconexiones_actuales)
                        elif accion == "eliminar":
                            eliminar_interconexion(interconexion, interconexiones_actuales)
                # Si no hay interconexiones existentes, se muestra un mensaje de error
                else:
                    print("No hay interconexiones existentes para modificar o eliminar.")
            # Se pregunta al usuario si desea continuar gestionando interconexiones
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

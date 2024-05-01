import variables
import menu_principal

def mostrar_interconexiones(interconexiones):
    if interconexiones:
        print("\nListado de interconexiones existentes:")
        for interc in interconexiones:
            print(interc['Id'] + ": " + interc['origen'] + " a " + interc['destino'] + " - " + str(interc['capacidad']) + "%")
    else:
        print("No hay interconexiones registradas.")
        return False
    return True


def seleccionar_interconexion(interconexiones):
    if mostrar_interconexiones(interconexiones):
        id_interconexion = input(
            "Introduce el identificador de la interconexión a modificar o eliminar: "
        ).upper()
        return next(
            (interc for interc in interconexiones if interc["id"] == id_interconexion),
            None,
        )
    return None


def modificar_interconexion(interc):
    nueva_capacidad = int(
        input("Introduce el nuevo porcentaje de la interconexión (1-100): ")
    )
    while nueva_capacidad <= 0 or nueva_capacidad > 100:
        print("Porcentaje inválido. Introduce un valor entre 1 y 100.")
        nueva_capacidad = int(
            input("Introduce el nuevo porcentaje de la interconexión (1-100): ")
        )
    interc["capacidad"] = nueva_capacidad
    print("Interconexión actualizada con éxito.")


def eliminar_interconexion(interconexiones, interc):
    interconexiones.remove(interc)
    print("Interconexión eliminada con éxito.")


def mostrar_recursos_disponibles(recursos):
    if recursos:
        print("\nListado de recursos disponibles para interconexión:")
        for recurso in recursos:
            print(recurso['Id'])
    else:
        print("No hay recursos disponibles para interconexión. Asegúrate de haber añadido recursos antes de intentar interconectarlos.")
        return False
    return True

def seleccionar_recurso(mensaje, recursos_destino):
    while True:
        print(mensaje)
        id_recurso = input("Introduce el identificador del recurso: ").upper()
        if any(r["Id"] == id_recurso for r in recursos_destino):
            return id_recurso
        print("Identificador no válido. Intente de nuevo.")

def validar_capacidad_interconexion(id_origen, id_destino, capacidad, interconexiones):
    uso_actual = sum(
        interc['capacidad'] for interc in interconexiones
        if interc['origen'] == id_origen and interc['destino'] == id_destino
    )
    capacidad_disponible = 100 - uso_actual
    if capacidad > capacidad_disponible:
        print("La capacidad total de interconexión excede el 100%. Solo puedes asignar hasta un " + str(capacidad_disponible) + "% adicional.")
        return capacidad_disponible
    return capacidad

def agregar_interconexion(id_origen, id_destino, capacidad, interconexiones, tipo):
    nuevo_id = id_origen + "-" + id_destino + "-" + str(len(interconexiones) + 1)
    if tipo == "FH":
        variables.interconexiones_fh.append({
            "id": nuevo_id,
            "origen": id_origen,
            "destino": id_destino,
            "capacidad": capacidad,
        })
    else:
        variables.interconexiones_pb.append({
            "id": nuevo_id,
            "origen": id_origen,
            "destino": id_destino,
            "capacidad": capacidad,
        }) 
    print("Interconexión " + nuevo_id + " agregada con éxito.")


def menu_interconexion():
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

        accion = input(
            "¿Deseas crear una nueva interconexión, editar o eliminar una existente? (Crear/Editar/Eliminar): "
        ).capitalize()
        if accion == "Crear":
            origen = seleccionar_recurso("Selecciona el recurso de origen:", recursos)
            destino = seleccionar_recurso("Selecciona el recurso de destino:", recursos_destino)
            capacidad = int(
                input("Introduce el porcentaje de la interconexión (1-100): ")
            )
            while capacidad <= 0 or capacidad > 100:
                print("Porcentaje inválido. Introduce un valor entre 1 y 100.")
                capacidad = int(
                    input("Introduce el porcentaje de la interconexión (1-100): ")
                )
            capacidad_validada = validar_capacidad_interconexion(
                origen, destino, capacidad, interconexiones_actuales
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

if __name__ == "__main__":
    menu_interconexion()
    menu_principal.menu_principal()

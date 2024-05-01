import variables
import menu_principal


def mostrar_centros_distribucion():
    print(
        "\nListado de los centros de distribución disponibles: "
        + ", ".join(variables.centros_distribucion)
        + ": "
    )


def solicitar_identificador_centro(alta):
    while True:
        que_identificador = input("Introduce el identificador del centro de distribución: ").upper()
        existe_en_registros = any(
            centro == que_identificador for centro in variables.centros_distribucion
        )
        existe_en_usuario = any(
            centro_usuarios["Id"] == que_identificador
            for centro_usuarios in variables.centros_distribucion_usuarios
        )
        if not existe_en_registros:
            print("Identificador no encontrado. Intente de nuevo con un identificador de la lista de centros de distribución disponibles.")
        elif existe_en_registros and not existe_en_usuario and alta:
            return que_identificador
        elif existe_en_registros and existe_en_usuario and not alta:
            return que_identificador
        elif existe_en_registros and existe_en_usuario and alta:
            print("Este identificador ya está en uso para un centro de distribución. Introduce un identificador nuevo.")
        elif existe_en_registros and not existe_en_usuario and not alta:
            print("No hay registros de uso para este identificador. Introduce un identificador que ya esté en uso.")

def alta_centro():
    mostrar_centros_distribucion()
    que_identificador = solicitar_identificador_centro(alta=True)

    reserva_max = int(input("Ingresa la capacidad máxima de reserva del centro (litros): "))
    while int(reserva_max) <= 0:
        print("Por favor, introduce una capacidad válida mayor a 0.")
        reserva_max = int(input(
            "Ingresa la capacidad máxima de reserva del centro (litros): "
        ))

    reserva_actual = int(input("Ingresa la reserva actual del centro (litros): "))
    while (int(reserva_actual) > int(reserva_max)):
        print(
            "Por favor, introduce una reserva válida que no exceda la capacidad máxima."
        )
        reserva_actual = int(input("Ingresa la reserva actual del centro (litros): "))

    consumo = int(input("Cantidad de litros que consume diariamente el centro: "))
    while int(consumo) <= 0 or int(consumo) > int(reserva_max):
        print("Introduce un consumo válido y que no exceda la capacidad máxima del centro.")
        consumo = int(input("Cantidad de litros que consume diariamente el centro: "))

    variables.centros_distribucion_usuarios.append(
        {
            "Id": que_identificador,
            "Capacidad máxima": int(reserva_max),
            "Reserva actual": int(reserva_actual),
            "Consumo diario": int(consumo),
        }
    )
    print("Centro de distribución añadido correctamente.")


def modificar():
    mostrar_centros_distribucion()
    que_identificador = solicitar_identificador_centro()

    modifica_o_baja = input(
        "¿Quieres modificar o dar de baja este centro? (Modificar/Baja) "
    ).lower()
    if modifica_o_baja == "baja":
        variables.centros_distribucion_usuarios = [
            centro
            for centro in variables.centros_distribucion_usuarios
            if centro["Id"] != que_identificador
        ]
        print("Centro de distribución eliminado correctamente.")
        return

    if modifica_o_baja == "modificar":
        actualizar_centro(que_identificador)


def actualizar_centro(que_identificador):
    reserva_max = input("Nueva capacidad máxima de reserva (litros): ")
    while int(reserva_max) <= 0:
        print("Introduce una capacidad máxima válida mayor a 0.")
        reserva_max = input("Nueva capacidad máxima de reserva (litros): ")

    reserva_actual = input("Nueva reserva actual (litros): ")
    while (int(reserva_actual) > int(reserva_max)):
        print("Introduce una reserva actual válida que no exceda la capacidad máxima.")
        reserva_actual = input("Nueva reserva actual (litros): ")

    consumo = input("Nueva cantidad de litros que consume diariamente el centro: ")
    while int(consumo) <= 0 or int(consumo) > (reserva_max):
        print("Introduce un consumo válido y que no exceda la capacidad máxima del centro.")
        consumo = input("Nueva cantidad de litros que consume diariamente el centro: ")

    for centro in variables.centros_distribucion_usuarios:
        if centro["Id"] == que_identificador:
            centro["Capacidad máxima"] = int(reserva_max)
            centro["Reserva actual"] = int(reserva_actual)
            centro["Consumo diario"] = int(consumo)
            print("Información actualizada correctamente.")
            break


def menu_centro_distribucion():
    while True:
        if variables.centros_distribucion_usuarios == []:
            opcion = input(
                "\n¿Quieres dar de alta un centro de distribución o salir al menú principal? "
            ).lower()
            if opcion == "dar de alta":
                alta_centro()
            elif opcion == "salir al menú principal":
                return  # Regresa al menú principal
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            opcion = input(
                "\n¿Quieres dar de alta un centro de distribución, modificar uno existente, o salir al menú principal? "
            ).lower()
            if opcion == "dar de alta":
                alta_centro()
            elif opcion == "modificar":
                modificar()
            elif opcion == "salir al menú principal":
                return  # Regresa al menú principal
            else:
                print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu_centro_distribucion()
    menu_principal.menu_principal()

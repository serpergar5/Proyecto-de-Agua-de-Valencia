import variables
import menu_principal


def mostrar_centros_distribucion():
    try:
        print(
            "\nListado de los centros de distribución disponibles: "
            + ", ".join(variables.centros_distribucion)
            + ": "
        )
    except:
        print("Error al mostrar los centros de distribución.")
        menu_principal.menu_principal()


def solicitar_identificador_centro(alta):
    try:
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
    except:
        print("Error al solicitar el identificador.")
        menu_principal.menu_principal()
    
def alta_centro():
    try:
        print("\n¿Quieres ver el listado de centros de distribución disponibles?")
        print("1) Sí")
        print("2) No")
        if(input("Elige una opción (1-2): ") == "1"):
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
    except:
        print("Error al dar de alta el centro de distribución.")
        menu_principal.menu_principal()

def modificar():
    try:
        mostrar_centros_distribucion()
        que_identificador = solicitar_identificador_centro(alta=False)
        print("\n¿Quieres modificar o dar de baja este centro?")
        print("1) Modificar")
        print("2) Dar de baja")
        modifica_o_baja = input("Elige una opción (1-2): ")

        if modifica_o_baja == "2":
            variables.centros_distribucion_usuarios = [
                centro
                for centro in variables.centros_distribucion_usuarios
                if centro["Id"] != que_identificador
            ]
            print("Centro de distribución eliminado correctamente.")
            return

        if modifica_o_baja == "1":
            actualizar_centro(que_identificador)
    except:
        print("Error al modificar el centro de distribución.")
        menu_principal.menu_principal()


def actualizar_centro(que_identificador):
    try:
        reserva_max = input("Nueva capacidad máxima de reserva (litros): ")
        while int(reserva_max) <= 0:
            print("Introduce una capacidad máxima válida mayor a 0.")
            reserva_max = input("Nueva capacidad máxima de reserva (litros): ")

        reserva_actual = input("Nueva reserva actual (litros): ")
        while (int(reserva_actual) > int(reserva_max)):
            print("Introduce una reserva actual válida que no exceda la capacidad máxima.")
            reserva_actual = input("Nueva reserva actual (litros): ")

        consumo = input("Nueva cantidad de litros que consume diariamente el centro: ")
        while int(consumo) <= 0 or int(consumo) > int((reserva_max)):
            print("Introduce un consumo válido y que no exceda la capacidad máxima del centro.")
            consumo = input("Nueva cantidad de litros que consume diariamente el centro: ")

        for centro in variables.centros_distribucion_usuarios:
            if centro["Id"] == que_identificador:
                centro["Capacidad máxima"] = int(reserva_max)
                centro["Reserva actual"] = int(reserva_actual)
                centro["Consumo diario"] = int(consumo)
                print("Información actualizada correctamente.")
                break
    except:
        print("Error al actualizar la información del centro de distribución.")
        menu_principal.menu_principal()


def menu_centro_distribucion():
    try:
        while True:
            if variables.centros_distribucion_usuarios == []:
                print("\nMenú Centros de Distribución")
                print("1) Dar de alta un centro de distribución")
                print("2) Salir al menú principal")
                opcion = input("Elige una opción (1-2): ")
                if opcion == "1":
                    alta_centro()
                elif opcion == "2":
                    return  # Regresa al menú principal
                else:
                    print("Por favor, selecciona una opción válida.")
            else:
                print("\nMenú Centros de Distribución")
                print("1) Dar de alta un centro de distribución")
                print("2) Modificar un centro de distribución")
                print("3) Salir al menú principal")
                opcion = input("Elige una opción (1-2-3): ")
                if opcion == "1":
                    alta_centro()
                elif opcion == "2":
                    modificar()
                elif opcion == "3":
                    return  # Regresa al menú principal
                else:
                    print("Por favor, selecciona una opción válida.")
    except:
        print("Error al mostrar el menú de centros de distribución.")
        menu_principal.menu_principal()

if __name__ == "__main__":
    menu_centro_distribucion()
    menu_principal.menu_principal()

import variables
import menu_principal


def mostrar_fuentes():
    print(
        "\nListado de fuentes hídricas disponibles: "
        + ", ".join(variables.fuentes_hidricas)
        + ": "
    )


def solicitar_identificador(alta):
    while True:
        que_identificador = input("Introduce el identificador: ").upper()
        existe_en_registros = any(
            fuente == que_identificador for fuente in variables.fuentes_hidricas
        )
        existe_en_usuario = any(
            fuente_usuarios["Id"] == que_identificador
            for fuente_usuarios in variables.fuentes_hidricas_usuarios
        )
        if not existe_en_registros:
            print("Identificador no encontrado. Intente de nuevo con un identificador de la lista de fuentes hídricas disponibles.")
        elif existe_en_registros and not existe_en_usuario and alta:
            return que_identificador
        elif existe_en_registros and existe_en_usuario and not alta:
            return que_identificador
        elif existe_en_registros and existe_en_usuario and alta:
            print("Este identificador ya está en uso para una fuente hídrica. Introduce un identificador nuevo.")
        elif existe_en_registros and not existe_en_usuario and not alta:
            print("No hay registros de uso para este identificador. Introduce un identificador que ya esté en uso.")


def alta_fuente():
    print("\n¿Quieres ver el listado de fuentes hídricas disponibles?")
    print("1) Sí")
    print("2) No")
    if(input("Elige una opción (1-2): ") == "1"):
        mostrar_fuentes()
    que_identificador = solicitar_identificador(alta=True)

    calidad = input(
        "Escoge la calidad del agua: " + ", ".join(variables.calidad_del_agua) + ": "
    ).title()
    while calidad not in variables.calidad_del_agua:
        print("Calidad no válida. Introduce una calidad válida.")
        calidad = input("Escoge la calidad del agua: ").title()

    litros = int(input("Cantidad de litros: "))
    while litros <= 0:
        print("Introduce una cifra mayor a 0.")
        litros = int(input("Cantidad de litros: "))

    variables.fuentes_hidricas_usuarios.append(
        {
            "Id": que_identificador,
            "Calidad": calidad,
            "Litros": litros,
        }
    )
    print("Fuente añadida correctamente.")


def modificar_fuente():
    mostrar_fuentes()
    que_identificador = solicitar_identificador(alta=False)
    print("\n¿Quieres modificar la calidad, los litros o dar de baja?")
    print("1) Calidad")
    print("2) Litros")
    print("3) Dar de baja")
    que_modifica = input("Elige una opción (1-2-3): ")
    
    while que_modifica not in ["1", "2", "3"]:
        print("Opción no válida. Elige una opción válida.")
        print("\n¿Quieres modificar la calidad, los litros o dar de baja?")
        print("1) Calidad")
        print("2) Litros")
        print("3) Dar de baja")
        que_modifica = input("Elige una opción (1-2-3): ")

    if que_modifica == "3":
        variables.fuentes_hidricas_usuarios = [
            fuente
            for fuente in variables.fuentes_hidricas_usuarios
            if fuente["Id"] != que_identificador
        ]
        print("Fuente eliminada correctamente.")
        return

    if que_modifica == "1":
        nueva_info = input("Introduce la nueva calidad " + str(variables.calidad_del_agua) + ": ").title()
        if nueva_info not in variables.calidad_del_agua:
            print("Calidad no válida.")
            return
        for fuente in variables.fuentes_hidricas_usuarios:
            if fuente["Id"] == que_identificador:
                fuente["Calidad"] = nueva_info
                print(que_identificador + " actualizada correctamente.")
            else:
                continue
        
    if que_modifica == "2":
        nueva_info = input("Introduce la nueva cantidad de litros: ")
        if int(nueva_info) <= 0:
            print("Introduce una cifra mayor a 0.")
            return
        for fuente in variables.fuentes_hidricas_usuarios:
            if fuente["Id"] == que_identificador:
                fuente["Litros"] = nueva_info
                print("Cantidad actualizada a " + str(nueva_info) + "L correctamente.")
            else:
                continue
            
def menu_fuente_hidrica():
    while True:
        if variables.fuentes_hidricas_usuarios == []:
            print("\nMenú Fuentes Hídricas")
            print("1) Dar de alta una fuente hídrica")
            print("2) Salir al menú principal")

            opcion = input("Elige una opción (1-2): ")
            if opcion == "1":
                alta_fuente()
            elif opcion == "2":
                return  # Salir al menú principal
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            print("\nMenú Fuentes Hídricas")
            print("1) Dar de alta una fuente hídrica")
            print("2) Modificar una fuente hídrica")
            print("3) Salir al menú principal")
            opcion = input("Elige una opción (1-2-3): ")
            if opcion == "1":
                alta_fuente()
            elif opcion == "2":
                modificar_fuente()
            elif opcion == "3":
                return  # Salir al menú principal
            else:
                print("Por favor, selecciona una opción válida.")


# Si es llamado directamente, vuelve al menú principal al finalizar
if __name__ == "__main__":
    menu_fuente_hidrica()
    menu_principal.menu_principal()

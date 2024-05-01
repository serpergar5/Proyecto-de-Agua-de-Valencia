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
    if (
        input("¿Quieres ver el listado de fuentes hídricas disponibles? (sí/no): ")
        .strip()
        .lower()
        == "sí"
    ):
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
            "Uso": variables.calidad_del_agua_indice[calidad],
        }
    )
    print("Fuente añadida correctamente.")


def modificar_fuente():
    mostrar_fuentes()
    que_identificador = solicitar_identificador(alta=False)

    que_modifica = input(
        "¿Quieres modificar la calidad, los litros, o dar de baja? "
    ).lower()
    while que_modifica not in ["calidad", "litros", "dar de baja"]:
        print("Opción no válida. Elige una opción válida.")
        que_modifica = input(
            "¿Quieres modificar la calidad, los litros, o dar de baja? "
        ).lower()

    if que_modifica == "dar de baja":
        variables.fuentes_hidricas_usuarios = [
            fuente
            for fuente in variables.fuentes_hidricas_usuarios
            if fuente["Id"] != que_identificador
        ]
        print("Fuente eliminada correctamente.")
        return

    nueva_info = input(f"Introduce la nueva {que_modifica}: ")
    if que_modifica == "calidad":
        if nueva_info not in variables.calidad_del_agua:
            print("Calidad no válida.")
            return
        nueva_info = variables.calidad_del_agua_indice[nueva_info]

    for fuente in variables.fuentes_hidricas_usuarios:
        if fuente["Id"] == que_identificador:
            fuente[que_modifica.capitalize()] = nueva_info
            print("Información actualizada correctamente.")
            break


def menu_fuente_hidrica():
    while True:
        if variables.fuentes_hidricas_usuarios == []:
            opcion = input(
                "\n¿Quieres dar de alta una fuente hídrica o salir al menú principal? "
            ).lower()
            if opcion == "dar de alta":
                alta_fuente()
            elif opcion == "salir al menú principal":
                return  # Salir al menú principal
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            opcion = input(
                "\n¿Quieres dar de alta una fuente hídrica, modificar una existente, o salir al menú principal? "
            ).lower()
            if opcion == "dar de alta":
                alta_fuente()
            elif opcion == "modificar":
                modificar_fuente()
            elif opcion == "salir al menú principal":
                return  # Salir al menú principal
            else:
                print("Por favor, selecciona una opción válida.")


# Si es llamado directamente, vuelve al menú principal al finalizar
if __name__ == "__main__":
    menu_fuente_hidrica()
    menu_principal.menu_principal()

import variables
import menu_principal


def mostrar_plantas():
    print(
        "\nListado de plantas potabilizadoras disponibles: "
        + ", ".join(variables.plantas_potabilizadoras)
        + ": "
    )


def solicitar_identificador(alta):
    while True:
        que_identificador = input("Introduce el identificador de la planta potabilizadora: ").upper()
        existe_en_registros = any(
            planta == que_identificador for planta in variables.plantas_potabilizadoras
        )
        existe_en_usuario = any(
            planta_usuarios["Id"] == que_identificador
            for planta_usuarios in variables.plantas_potabilizadoras_usuarios
        )
        if not existe_en_registros:
            print("Identificador no encontrado. Intente de nuevo con un identificador de la lista de plantas potabilizadoras disponibles.")
        elif existe_en_registros and not existe_en_usuario and alta:
            return que_identificador
        elif existe_en_registros and existe_en_usuario and not alta:
            return que_identificador
        elif existe_en_registros and existe_en_usuario and alta:
            print("Este identificador ya está en uso para una planta potabilizadora. Introduce un identificador nuevo.")
        elif existe_en_registros and not existe_en_usuario and not alta:
            print("No hay registros de uso para este identificador. Introduce un identificador que ya esté en uso.")


def alta_planta():
    if (
        input(
            "¿Quieres ver el listado de plantas potabilizadoras disponibles? (sí/no): "
        ).lower()
        == "sí"
    ):
        mostrar_plantas()
    que_identificador = solicitar_identificador(alta=True)

    eficiencia = input(
        "Ingresa la eficiencia de la planta potabilizadora (Alta, Media, Baja): "
    ).title()
    while eficiencia not in variables.eficiencia:
        print("Por favor, introduce una eficiencia valida.")
        eficiencia = input("Ingresa la eficiencia: ").title()
    eficiencia_valor = variables.eficiencia_de_la_planta_indice[eficiencia]

    litros = int(input("Cantidad de litros que potabiliza la planta: "))
    while int(litros) <= 0:
        print("Introduce una cifra valida mayor a 0")
        litros = input("Cantidad de litros que potabiliza la planta: ")

    variables.plantas_potabilizadoras_usuarios.append(
        {
            "Id": que_identificador,
            "Eficiencia": eficiencia,
            "Litros": int(litros),
            "Uso": eficiencia_valor,
        }
    )
    print("Planta añadida correctamente.")


def modificar_planta():
    mostrar_plantas()
    que_identificador = solicitar_identificador(alta=False)

    que_modifica = input(
        "¿Quieres modificar la eficiencia, los litros, o quieres dar de baja? "
    ).lower()
    while que_modifica not in ["eficiencia", "litros", "dar de baja"]:
        print("Opción no válida. Elige una opción válida.")
        que_modifica = input(
            "¿Quieres modificar la eficiencia, los litros, o dar de baja? "
        ).lower()

    if que_modifica == "dar de baja":
        variables.plantas_potabilizadoras_usuarios = [
            planta
            for planta in variables.plantas_potabilizadoras_usuarios
            if planta["Id"] != que_identificador
        ]
        print("Planta eliminada correctamente.")
        return

    actualizar_planta(que_identificador, que_modifica)


def actualizar_planta(que_identificador, que_modifica):
    nueva_info = input("Introduce el nuevo valor: ").strip()
    if que_modifica == "eficiencia":
        if nueva_info not in variables.eficiencia:
            print("Eficiencia no válida.")
            return
        nueva_info = variables.eficiencia_de_la_planta_indice[nueva_info]
    elif que_modifica == "litros":
        if not nueva_info.isdigit() or int(nueva_info) <= 0:
            print("Introduce un número válido mayor a 0.")
            return
        nueva_info = int(nueva_info)

    for planta in variables.plantas_potabilizadoras_usuarios:
        if planta["Id"] == que_identificador:
            planta[que_modifica.capitalize()] = nueva_info
            print("Información actualizada correctamente.")
            break


def menu_planta_potabilizadora():
    while True:
        if variables.plantas_potabilizadoras_usuarios == []:
            opcion = input(
                "\n¿Quieres dar de alta una planta potabilizadora, o salir al menú principal? "
            ).lower()
            if opcion == "dar de alta":
                alta_planta()
            elif opcion == "salir al menú principal":
                return  # Regresa al menú principal
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            opcion = input(
                "\n¿Quieres dar de alta una planta potabilizadora, modificar una existente, o salir al menú principal? "
            ).lower()
            if opcion == "dar de alta":
                alta_planta()
            elif opcion == "modificar":
                modificar_planta()
            elif opcion == "salir al menú principal":
                return  # Regresa al menú principal
            else:
                print("Por favor, selecciona una opción válida.")


# Integración con el menú principal si es llamado directamente
if __name__ == "__main__":
    menu_planta_potabilizadora()
    menu_principal.menu_principal()

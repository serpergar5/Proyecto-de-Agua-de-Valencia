import variables
import menu_principal


def alta():
    i = 0

    mostrar_listado = str(
        input(
            "¿Quieres ver el listado de los centros de distribución disponibles? "
        ).title()
    )

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(variables.centros_distribucion)
            que_identificador = input("Introduce el identificador: ").upper()
            comprobar_si_existe = False

            comprobar_si_existe = any(
                dato_usuarios["Centro de distribución"] == que_identificador
                for dato_usuarios in variables.centros_distribucion_usuarios
            )
            mostrar_listado = "No"

            if comprobar_si_existe:
                print(
                    "Ya has introducido datos para este centro de distribución. Introduce otro identificador de la lista: "
                    + str(variables.centros_distribucion)
                )
                continue

            if que_identificador not in variables.centros_distribucion:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.centros_distribucion,
                )
            else:
                i += 1

        if i == 1:
            reserva_max = float(
                input(
                    "Ingresa la capacidad máxima de reserva del centro de distribución: "
                )
            )
            if reserva_max <= 0:
                (print("Por favor, introduce una capcidad de reserva valida."))
            else:
                reserva_actual = float(
                    input(
                        "Ingresa la reserva de agua actual del centro de distribución: "
                    ).title()
                )
                if reserva_actual < 0 and reserva_actual >= reserva_max:
                    (print("Por favor, introduce una capcidad de reserva valida."))
                else:
                    i += 1

        if i == 2:
            consumo = (input("Cantidad de litros que consume diariamente: ")).strip()
            if consumo == "":
                print("Introduce una cifra valida")
            elif float(consumo) < 0:
                print("Introduce una cifra valida")
            else:
                i += 1

        if i == 3:
            variables.centros_distribucion.append(
                {
                    "Centro de distribución": que_identificador,
                    "Capacidad máxima": reserva_max,
                    "Reserva actual": reserva_actual,
                    "Consumo diario": consumo,
                }
            )
            añadir_mas_datos = str(
                input(
                    "¿Quieres darme los datos de otra planta potabilizadora o salir al menu principal?: "
                )
            )
            if añadir_mas_datos == "Dar más datos":
                i = 0
            else:
                menu_principal.menu()


def modificar():
    i = 0

    mostrar_listado = str(
        input("¿Quieres ver el listado de los centros de distribución disponibles? ")
    ).title()

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(variables.centros_distribucion)
            que_identificador = input(
                "Introduce un identificador ya creado para modificarlo: "
            ).title()
            if que_identificador not in variables.centros_distribucion:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.centros_distribucion,
                )

            mostrar_listado = "No"
            comprobar_si_existe = any(
                dato_usuarios["Centro de distribución"] == que_identificador
                for dato_usuarios in variables.centros_distribucion_usuarios
            )
            if comprobar_si_existe == False:
                continue

            if que_identificador not in variables.centros_distribucion:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.centros_distribucion,
                )
            else:
                modifica_o_baja = input(
                    "¿Quieres modificar o dar de baja un centro de distribución?"
                ).title()
                if modifica_o_baja == "Modificar":
                    i == 1

                elif modifica_o_baja == "Dar De Baja":
                    for dato_usuarios in variables.centros_distribucion_usuarios:
                        if dato_usuarios["Centro de distribución"] == que_identificador:
                            variables.centros_distribucion_usuarios.remove(
                                dato_usuarios
                            )
                            print("Datos para " + que_identificador + " eliminados.")
                            menu_principal.menu()
                if i == 1:
                    reserva_max = float(
                        input(
                            "Escoge la capacidad máxima que admite el centro de distribución: "
                        ).strip()
                    )
                    if reserva_max <= 0:
                        print("Introduce una eficiencia válida.")
                    else:
                        i += 1

                if i == 2:
                    reserva_actual = float(
                        input("Escoge la reseerva actual de agua que hay: ").strip()
                    )
                    if reserva_actual == "":
                        print("Introduce una cifra valida")
                    elif reserva_actual > reserva_max:
                        print(
                            "Introduce una cifra menor que la capacidad máxima admitida que es "
                        ) + str(reserva_max)
                    else:
                        i += 1
                if i == 3:
                    consumo = (
                        input("Cantidad de litros que consume diariamente: ")
                    ).strip()
                    if consumo == "":
                        print("Introduce un consumo valida")
                    elif float(consumo) <= 0:
                        print("Introduce un consumo valido")
                    else:
                        i += 1
                if i == 4:
                    for dato_usuarios in variables.plantas_potabilizadoras_usuarios:
                        if dato_usuarios["Centro de distribución"] == que_identificador:
                            dato_usuarios["Capacidad máxima"] = reserva_max
                            dato_usuarios["Reserva actual"] = (reserva_actual,)
                            dato_usuarios["Consumo diario"] = consumo

                    añadir_mas_datos = str(
                        input(
                            "¿Quieres darme los datos de otra planta potabilizadora o salir al menu principal?: "
                        )
                    )
                    if añadir_mas_datos == "Dar más datos":
                        i = 0
                    else:
                        menu_principal.menu()

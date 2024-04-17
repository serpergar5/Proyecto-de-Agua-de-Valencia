import variables
import menu_principal

def alta():
    i = 0

    mostrar_listado = str(
        input("¿Quieres ver el listado de plantas potabilizadoras disponibles?: ").title())

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(variables.plantas_potabilizadoras)
            que_identificador = input("Introduce el identificador: ").upper()
            comprobar_si_existe = False
            
            comprobar_si_existe = any(dato_usuarios["Planta potabilizadora"] == que_identificador for dato_usuarios in variables.plantas_potabilizadoras_usuarios)
            mostrar_listado = "No"
            
            if comprobar_si_existe:
                print(
                    "Ya has introducido datos para esta planta potabilizadora. Introduce otro identificador de la lista. "
                    + str(variables.plantas_potabilizadoras)
                )
                continue

            if que_identificador not in variables.plantas_potabilizadoras:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.plantas_potabilizadoras,
                )
            else:
                i += 1

        if i == 1:
            eficiencia = (
                input(
                    "Ingresa la eficiencia de la planta potabilizadora "
                    + str(variables.eficiencia)
                .title()
                + ": "
            ).title())
            if eficiencia not in variables.eficiencia:
                (
                    print(
                        "Por favor, introduce una eficiencia valida."
                    )
                )
            else:
                i += 1

        if i == 2:
            litros = (input("Cantidad de litros que potabiliza la planta: ")).strip()
            if litros == "":
                print("Introduce una cifra valida")
            elif int(litros) <= 0:
                print("Introduce una cifra mayor a 0")
            else:
                i += 1

        if i == 3:
            variables.plantas_potabilizadoras_usuarios.append(
                {
                    "Planta potabilizadora": que_identificador,
                    "Eficiencia": eficiencia,
                    "Litros": litros,
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
        input("¿Quieres ver el listado de plantas potabilizadoras disponibles? ")
    ).title()

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(variables.plantas_potabilizadoras)
            que_identificador = input(
                "Introduce el identificador que quieres modificar: "
            ).upper()

            comprobar_si_existe = any(
                dato_usuarios["Planta potabilizadora"] == que_identificador
                for dato_usuarios in variables.plantas_potabilizadoras_usuarios
            )
            if comprobar_si_existe == False:
                continue

            if que_identificador not in variables.plantas_potabilizadoras:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.plantas_potabilizadoras,
                )
            else:
                que_modifica = input(
                    "¿Quieres modificar la calidad, los litros, o quieres dar de baja?: "
                ).title()
                if que_modifica == "Calidad":
                    i += 1
                elif que_modifica == "Litros":
                    i += 2
                elif que_modifica == "Dar De Baja":
                    for dato_usuarios in variables.plantas_potabilizadoras_usuarios:
                        if dato_usuarios["Planta potabilizadora"] == que_identificador:
                            variables.plantas_potabilizadoras_usuarios.remove(dato_usuarios)
                            print("Datos para " + que_identificador + " eliminados.")
                            menu_principal.menu()

        if i == 1:
            eficiencia = input(
                "Escoge la calidad que tiene el río "
                + str(variables.eficiencia)
                + ": "
            ).title()
            if eficiencia not in variables.eficiencia:
                print("Introduce una eficiencia válida.")
            else:
                break

        if i == 2:
            litros = (input("Cantidad de litros: ")).strip()
            if litros == "":
                print("Introduce una cifra valida")
            elif int(litros) <= 0:
                print("Introduce una cifra mayor a 0")
            else:
                i += 1

        if i == 3:
            for dato_usuarios in variables.plantas_potabilizadoras_usuarios:
                if dato_usuarios["Planta potabilizadora"] == que_identificador:
                    dato_usuarios["Eficiencia"] = eficiencia,
                    dato_usuarios["Litros"] = litros

            añadir_mas_datos = str(
                input(
                    "¿Quieres darme los datos de otra planta potabilizadora o salir al menu principal?: "
                )
            )
            if añadir_mas_datos == "Dar más datos":
                i = 0
            else:
                menu_principal.menu()

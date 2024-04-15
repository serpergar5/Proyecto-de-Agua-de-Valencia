import variables
import menu_principal

def alta():
    i = 0

    mostrar_listado = str(
        input("¿Quieres ver el listado de plantas potabilizadoras disponibles? ").title())

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(variables.plantas_potabilizadoras)
            que_identificador = input("Introduce el identificador: ").title()
            if que_identificador not in variables.plantas_potabilizadoras:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.plantas_potabilizadoras,
                )
                
            comprobar_si_existe = any(dato_usuarios["Fuente hídrica"] == que_identificador for dato_usuarios in variables.fuentes_hidricas_usuarios)

            if comprobar_si_existe:
                print(
                    "Ya has introducido datos para esta planta potabilizadora. Introduce otro identificador de la lista."
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
                ).title()
                + ": "
            )
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
            variables.fuentes_hidricas_usuarios.append(
                {
                    "Fuente hídrica": que_identificador,
                    "Calidad": eficiencia,
                    "Litros": litros,
                }
            )
            añadir_mas_datos = str(
                input(
                    "¿Quieres darme los datos de otra fuente hídrica o salir al menu principal?: "
                )
            )
            if añadir_mas_datos == "Dar más datos":
                i = 0
            else:
                menu_principal.menu()
                

def modificar():
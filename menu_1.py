import variables
import menu_principal

def alta():
    i = 0

    mostrar_listado = str(
        input("¿Quieres ver el listado de fuentes hídricas disponibles? ")
    ).title()

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(variables.fuentes_hidricas)
            que_identificador = input("Introduce el identificador: ").upper()
            comprobar_si_existe = False

            if que_identificador not in variables.fuentes_hidricas:
                
                comprobar_si_existe = any(dato_usuarios["Fuente hídrica"] == que_identificador for dato_usuarios in variables.fuentes_hidricas_usuarios)
            
            if comprobar_si_existe:
                print("Ya has introducido datos para esta fuente hídrica. Introduce otro identificador de la lista." + str(variables.fuentes_hidricas))
                continue
                
            if que_identificador not in variables.fuentes_hidricas:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.fuentes_hidricas,
                )
            else:
                i += 1

        if i == 1:
            calidad = input(
                "Escoge la calidad que tiene el río " + str(variables.calidad_del_agua) + ": "
            ).title()
            if calidad not in variables.calidad_del_agua:
                print("Introduce una calidad válida.")
            else:
                i += 1

        if i == 2:
            litros = (input("Cantidad de litros: ")).strip()
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
                    "Calidad": calidad, #TODO FIX Guarda como tupla
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
    i = 0

    mostrar_listado = str(
        input("¿Quieres ver el listado de fuentes hídricas disponibles? ")
    ).title()

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(variables.fuentes_hidricas)
            que_identificador = input("Introduce el identificador que quieres modificar: ").upper()
            
            comprobar_si_existe = any(
                dato_usuarios["Fuente hídrica"] == que_identificador
                for dato_usuarios in variables.fuentes_hidricas_usuarios
        )
            if comprobar_si_existe == False:
                continue

            if que_identificador not in variables.fuentes_hidricas:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    variables.fuentes_hidricas,
                )
            else:
                que_modifica = input("¿Quieres modificar la calidad, los litros, o quieres dar de baja?: ").title()
                if que_modifica == "Calidad":
                    i += 1
                elif que_modifica == "Litros":
                    i += 2
                elif que_modifica == "Dar De Baja":
                    for dato_usuarios in variables.fuentes_hidricas_usuarios:
                        if dato_usuarios["Fuente hídrica"] == que_identificador:
                            variables.fuentes_hidricas_usuarios.remove(dato_usuarios)
                            print("Datos para " + que_identificador  + " eliminados.")
                            menu_principal.menu()

        if i == 1:
            calidad = input(
                "Escoge la calidad que tiene el río " + str(variables.calidad_del_agua) + ": "
            ).title()
            if calidad not in variables.calidad_del_agua:
                print("Introduce una calidad válida.")
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
            for dato_usuarios in variables.fuentes_hidricas_usuarios:
                if dato_usuarios["Fuente hídrica"] == que_identificador:
                    dato_usuarios["Calidad"] = calidad,
                    dato_usuarios["Litros"] = litros

            añadir_mas_datos = str(
                input(
                    "¿Quieres darme los datos de otra fuente hídrica o salir al menu principal?: "
                )
            )
            if añadir_mas_datos == "Dar más datos":
                i = 0
            else:
                menu_principal.menu()

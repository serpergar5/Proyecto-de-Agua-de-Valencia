datos_usuarios = []


def menu():
    seleccion = int(
        input(
            """
Elige una opción:
-----------------
1) Fuente hídrica
2) Planta potabilizadora
3) Centro de distribución
4) Interconexión
5) Días
6) Info sistema
7) Ficheros
0) Salir

"""
        )
    )

    if seleccion == 0:
        print("Hasta luego")
        exit()

    elif seleccion == 1:
        menu1()

    elif seleccion == 2:
        menu2()


def menu1():
    fuentes_hidricas = ["Ebro", "Magro", "Jucar", "Turia"]
    calidad_del_agua = ["Potable", "Alta", "Media", "Baja", "No Potabilizable"]
    i = 0

    mostrar_listado = str(
        input("¿Quieres ver el listado de fuentes hídricas disponibles? ")
    ).title()

    while True:
        if i == 0:
            if mostrar_listado == "Sí":
                print(fuentes_hidricas)
            que_identificador = input("Introduce el identificador: ").title()
            if que_identificador not in fuentes_hidricas:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    fuentes_hidricas,
                )
                
            comprobar_si_existe = any(dato_usuarios["Fuente hídrica"] == que_identificador for dato_usuarios in datos_usuarios)
            if comprobar_si_existe:
                print("Ya has introducido datos para esta fuente hídrica. Introduce otro identificador de la lista." + str(fuentes_hidricas))
                continue
                
            if que_identificador not in fuentes_hidricas:
                print(
                    "Por favor, introduce un identificador de la siguiente lista: ",
                    fuentes_hidricas,
                )
            else:
                i += 1

        if i == 1:
            calidad = input(
                "Escoge la calidad que tiene el río " + str(calidad_del_agua) + ": "
            ).title()
            if calidad not in calidad_del_agua:
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
            datos_usuarios.append(
                {
                    "Fuente hídrica": que_identificador,
                    "Calidad": calidad,
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
                menu()


def menu2():
    eficiencia_lista = ["Alta", "Media", "Baja"]
    i = 0

    plantas = []

    while True:
        if i == 0:
            id_potabilizadora = str(
                input("Introduce un id para la planta potabilizadora: ")
            )
            if (
                not id_potabilizadora.isalnum()
                or not len(id_potabilizadora) >= 3
                or id_potabilizadora in plantas
            ):
                print("Por favor, introduce un identificador valido")
            else:
                i += 1

        if i == 1:
            eficiencia = (
                input(
                    "Ingresa la eficiencia de la planta potabilizadora "
                    + str(eficiencia_lista)
                ).title()
                + ": "
            )
            if eficiencia not in eficiencia_lista:
                (
                    print(
                        "Por favor, introduce una eficiencia valida "
                        + str(eficiencia_lista)
                    ).title()
                    + ": "
                )
            else:
                i += 1

        if i == 2:
            cantidad = int(
                input("Cantidad de litros que potabiliza la planta potabilizadora: ")
            )
            if calidad not in calidad_del_agua:
                print("Introduce una calidad válida.")
            else:
                i += 1

            if añadir_mas_datos == "Dar más datos":
                i = 0
            else:
                menu()


menu()

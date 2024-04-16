import variables
import menu_1
import menu_2
import menu_3

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
        if len(variables.fuentes_hidricas_usuarios) == 0:
            menu_1.alta()
        else:
            while True:
                modificar_alta = input(
                    "¿Quieres dar de alta una fuente hídrica o modificarla? "
                ).title()
                if modificar_alta == "Dar De Alta":
                    menu_1.alta()
                    break
                elif modificar_alta == "Modificarla":
                    menu_1.modificar()
                    break
                else:
                    print("Por favor, selecciona una opción válida.")

    elif seleccion == 2:
        if len(variables.plantas_potabilizadoras_usuarios) == 0:
            menu_2.alta()
        else:
            while True:
                modificar_alta = input(
                    "¿Quieres dar de alta una planta potabilizadora o modificarla? "
                ).title()
                if modificar_alta == "Dar De Alta":
                    menu_2.alta()
                    break
                elif modificar_alta == "Modificarla":
                    menu_2.modificar()
                    break
                else:
                    print("Por favor, selecciona una opción válida.")

    elif seleccion == 3:
        if len(variables.centros_distribucion_usuarios) == 0:
            menu_3.alta()
        else:
            while True:
                modificar_alta = input(
                    "¿Quieres dar de alta un centro de distribución o modificarlo? "
                ).title()
                if modificar_alta == "Dar De Alta":
                    menu_2.alta()
                    break
                elif modificar_alta == "Modificarla":
                    menu_2.modificar()
                    break
                else:
                    print("Por favor, selecciona una opción válida.")

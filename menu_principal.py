import menu_1
import menu_2
import menu_3
import menu_4
import menu_5
import menu_6
import menu_7

def mostrar_menu():
    print(
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


def solicitar_seleccion():
    while True:
        try:
            seleccion = int(input("Ingresa tu elección: "))
            if 0 <= seleccion <= 7:
                return seleccion
            else:
                print("Por favor, ingresa un número entre 0 y 7.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


def procesar_opcion(seleccion):
    if seleccion == 0:
        print("Hasta luego.")
        exit()
    elif seleccion == 1:
        menu_1.menu_fuente_hidrica()
    elif seleccion == 2:
        menu_2.menu_planta_potabilizadora()
    elif seleccion == 3:
        menu_3.menu_centro_distribucion()
    elif seleccion == 4:
        menu_4.menu_interconexion()
    elif seleccion == 5:
        menu_5.menu_dias()
    elif seleccion == 6:
        menu_6.menu_info_sistema()
    elif seleccion == 7:
        menu_7.menu_ficheros



def menu_principal():
    while True:
        mostrar_menu()
        seleccion = solicitar_seleccion()
        procesar_opcion(seleccion)


if __name__ == "__main__":
    menu_principal()

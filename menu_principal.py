import menu_1, menu_2, menu_3, menu_4 ,menu_5 ,menu_6, menu_7

# Muestra el siguiente menú de opciones al usuario.
def mostrar_menu():
    try:
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
    except:
        print("Error al mostrar el menú.")


# Recoge la selección del usuario y la devuelve.
def solicitar_seleccion():
    try:
        while True:
            seleccion = int(input("Ingresa tu elección: "))
            if 0 <= seleccion <= 7:
                return seleccion
            else:
                print("Por favor, ingresa un número entre 0 y 7.")
    except:
        print("Error al solicitar la selección.")


# Procesa la selección del usuario y llama a la función correspondiente.
def procesar_opcion(seleccion):
    if seleccion == 0:
        print("Hasta luego.")
        exit(0)
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
        menu_7.menu_ficheros()


# Muestra el menú principal y procesa la selección del usuario.
def menu():
    while True:
        mostrar_menu()
        seleccion = solicitar_seleccion()
        procesar_opcion(seleccion)


# Si este script es el punto de entrada, ejecuta la función menu_principal (este archivo).
if __name__ == "__main__":
    menu()

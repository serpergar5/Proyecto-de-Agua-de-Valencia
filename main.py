menu = int(input(
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
))

if menu == 1:

    i = 0
    print("""

Introduce los siguientes datos\n
------------------------------
""")

    calidad_del_agua = ["Potable", "Alta", "Media", "Baja", "No Potabilizable"]

    while i >= 0:
        if i == 0:
            (input("Introdudce el identificador: "))
            i += 1
        elif i == 1:
            calidad = input("Escoge la calidad que tiene el río " + str(calidad_del_agua) + ": ")
            if calidad in calidad_del_agua:
                i += 1
            else: print("Introduce una calidad válida.")
        elif i == 2:
            int (input("Cantidad de litros: "))
            i += 1
        elif i == 3:
            break

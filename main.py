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
        i += 1
        if i == 1:
            (input("Introdudce el identificador: "))
        elif i == 2:
            (input("Escoge la calidad que tiene el río " + str(calidad_del_agua) + ": "))
        elif i == 3:
            int (input("Cantidad de litros: "))
        elif i == 4:
            break
        
    
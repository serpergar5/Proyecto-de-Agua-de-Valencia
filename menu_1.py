import variables
import menu_principal

#Muestra las fuentes hídricas que hay
def mostrar_fuentes():
    try:
        print(
            "\nListado de fuentes hídricas disponibles: "
            + ", ".join(variables.fuentes_hidricas)
            + ": "
        )
    except:
        print("Error al mostrar las fuentes hídricas.")
        menu_principal.menu_principal()

#Se encarga de solicitar el identificador de la fuente hídrica
def solicitar_identificador(alta):
    try:
        while True:
            #solicita el identificador
            que_identificador = input("Introduce el identificador: ").upper()
            #comprueba si el identificador existe en la lista de fuentes hídricas
            existe_en_registros = any(
                fuente == que_identificador for fuente in variables.fuentes_hidricas
            )
            #compueba si el identificador existe en la lista de fuentes hídricas de los usuarios
            existe_en_usuario = any(
                fuente_usuarios["Id"] == que_identificador
                for fuente_usuarios in variables.fuentes_hidricas_usuarios
            )
            #si el identificador no existe en la lista de fuentes hídricas
            if not existe_en_registros:
                print("Identificador no encontrado. Intente de nuevo con un identificador de la lista de fuentes hídricas disponibles.")
            #si el identificador existe en la lista de fuentes hídricas y no en la lista de fuentes hídricas de los usuarios y se quiere dar de alta
            elif existe_en_registros and not existe_en_usuario and alta:
                return que_identificador
            #si el identificador existe en la lista de fuentes hídricas y en la lista de fuentes hídricas de los usuarios y se quiere modificar
            elif existe_en_registros and existe_en_usuario and not alta:
                return que_identificador
            #si el identificador existe en la lista de fuentes hídricas y en la lista de fuentes hídricas de los usuarios y se quiere dar de alta indicando que ya está en uso
            elif existe_en_registros and existe_en_usuario and alta:
                print("Este identificador ya está en uso para una fuente hídrica. Introduce un identificador nuevo.")
            #si el identificador existe en la lista de fuentes hídricas y no en la lista de fuentes hídricas de los usuarios y se quiere modificar indicando que no hay registros para esa fuente
            elif existe_en_registros and not existe_en_usuario and not alta:
                print("No hay registros de uso para este identificador. Introduce un identificador que ya esté en uso.")
    except:
        print("Error al solicitar el identificador.")
        menu_principal.menu_principal()

#Da de alta una fuente hídrica
def alta_fuente():
    try:
        print("\n¿Quieres ver el listado de fuentes hídricas disponibles?")
        print("1) Sí")
        print("2) No")
        if(input("Elige una opción (1-2): ") == "1"):
            mostrar_fuentes()
        que_identificador = solicitar_identificador(alta=True)
        #solicita la calidad del agua
        calidad = input(
            "Escoge la calidad del agua: " + ", ".join(variables.calidad_del_agua) + ": "
        ).title()
        #comprueba si la calidad del agua es válida si no es valida pide que se introduzca una calidad válida
        while calidad not in variables.calidad_del_agua:
            print("Calidad no válida. Introduce una calidad válida.")
            calidad = input("Escoge la calidad del agua: ").title()
        #solicita la cantidad de litros si la cantidad de litros es menor o igual a 0 pide que se introduzca una cantidad mayor a 0
        litros = int(input("Cantidad de litros: "))
        while litros <= 0:
            print("Introduce una cifra mayor a 0.")
            litros = int(input("Cantidad de litros: "))
        #añade la fuente hídrica a la lista de fuentes hídricas de los usuarios
        variables.fuentes_hidricas_usuarios.append(
            {
                "Id": que_identificador,
                "Calidad": calidad,
                "Litros": litros,
            }
        )
        print("Fuente añadida correctamente.")
    except:
        print("Error al dar de alta una fuente hídrica.")
        menu_principal.menu_principal()

#Modifica una fuente hídrica
def modificar_fuente():
    try:
        #muestra las fuentes hídricas
        mostrar_fuentes()
        que_identificador = solicitar_identificador(alta=False)
        print("\n¿Quieres modificar la calidad, los litros o dar de baja?")
        print("1) Calidad")
        print("2) Litros")
        print("3) Dar de baja")
        que_modifica = input("Elige una opción (1-2-3): ")
        #comprueba si la opción es válida si no es válida pide que se introduzca una opción válida
        while que_modifica not in ["1", "2", "3"]:
            print("Opción no válida. Elige una opción válida.")
            print("\n¿Quieres modificar la calidad, los litros o dar de baja?")
            print("1) Calidad")
            print("2) Litros")
            print("3) Dar de baja")
            que_modifica = input("Elige una opción (1-2-3): ")
        #si la opción es 3 elimina la fuente hídrica y comprueba si la fuente hídrica existe en la lista de fuentes hídricas de los usuarios
        if que_modifica == "3":
            variables.fuentes_hidricas_usuarios = [
                fuente
                for fuente in variables.fuentes_hidricas_usuarios
                if fuente["Id"] != que_identificador
            ]
            print("Fuente eliminada correctamente.")
            return
        #si la opción es 1 pide la nueva calidad y comprueba si la calidad es válida si no es válida pide que se introduzca una calidad válida
        if que_modifica == "1":
            nueva_info = input("Introduce la nueva calidad " + str(variables.calidad_del_agua) + ": ").title()
            if nueva_info not in variables.calidad_del_agua:
                print("Calidad no válida.")
                return
            for fuente in variables.fuentes_hidricas_usuarios:
                if fuente["Id"] == que_identificador:
                    fuente["Calidad"] = nueva_info
                    print(que_identificador + " actualizada correctamente.")
                else:
                    continue
        #si la opción es 2 pide la nueva cantidad de litros y comprueba si la cantidad de litros es mayor a 0 si no es mayor a 0 pide que se introduzca una cantidad mayor a 0
        if que_modifica == "2":
            nueva_info = input("Introduce la nueva cantidad de litros: ")
            if int(nueva_info) <= 0:
                print("Introduce una cifra mayor a 0.")
                return
            for fuente in variables.fuentes_hidricas_usuarios:
                if fuente["Id"] == que_identificador:
                    fuente["Litros"] = nueva_info
                    print("Cantidad actualizada a " + str(nueva_info) + "L correctamente.")
                else:
                    continue
    except:
        print("Error al modificar la fuente hídrica.")
        menu_principal.menu_principal()
    
#Menú de fuentes hídricas
def menu_fuente_hidrica():
    try:
        #si no hay fuentes hídricas muestra el menú de fuentes hídricas sin la opción de modificar
        while True:
            if variables.fuentes_hidricas_usuarios == []:
                print("\nMenú Fuentes Hídricas")
                print("1) Dar de alta una fuente hídrica")
                print("2) Salir al menú principal")

                opcion = input("Elige una opción (1-2): ")
                if opcion == "1":
                    alta_fuente()
                elif opcion == "2":
                    return  # Salir al menú principal
                else:
                    print("Por favor, selecciona una opción válida.")
        #si hay fuentes hídricas ya registradas muestra el menú de fuentes hídricas con la opción de modificar
            else:
                print("\nMenú Fuentes Hídricas")
                print("1) Dar de alta una fuente hídrica")
                print("2) Modificar una fuente hídrica")
                print("3) Salir al menú principal")
                opcion = input("Elige una opción (1-2-3): ")
                if opcion == "1":
                    alta_fuente()
                elif opcion == "2":
                    modificar_fuente()
                elif opcion == "3":
                    return  # Salir al menú principal
                else:
                    print("Por favor, selecciona una opción válida.")
    except:
        print("Error al mostrar el menú de fuentes hídricas.")
        menu_principal.menu_principal()


# Si es llamado directamente, vuelve al menú principal al finalizar
if __name__ == "__main__":
    menu_fuente_hidrica()
    menu_principal.menu_principal()

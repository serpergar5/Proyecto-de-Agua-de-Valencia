import variables
import menu_principal

# Muestra las plantas potabilizadoras disponibles
def mostrar_plantas():
    try:
        print("\nListado de plantas potabilizadoras ya introducidas: ")
        for planta in variables.plantas_potabilizadoras_usuarios:
            print(planta["Id"])
    except:
        print("Error al mostrar las plantas potabilizadoras.")
        menu_principal.menu_principal()

# Solicita el identificador de la planta potabilizadora
def solicitar_identificador(alta):
    try:
        while True:
            # Solicita el identificador
            que_identificador = input("Introduce el identificador de la planta potabilizadora: ")
            #Comprueba si el identificador existe en la lista de plantas potabilizadoras
            while len(que_identificador) < 3:
                print("El identificador debe tener al menos 3 caracteres.")
                que_identificador = input("Introduce el identificador de la planta potabilizadora: ")
            #Comprueba si el identificador existe en la lista de plantas potabilizadoras de los usuarios
            existe_en_usuario = any(
                planta_usuarios["Id"] == que_identificador
                for planta_usuarios in variables.plantas_potabilizadoras_usuarios
            )

            #Si el identificador existe en la lista de plantas potabilizadoras y no en la lista de plantas potabilizadoras de los usuarios y se quiere dar de alta
            if not existe_en_usuario and alta:
                return que_identificador
            #Si el identificador existe en la lista de plantas potabilizadoras y en la lista de plantas potabilizadoras de los usuarios y se quiere modificar
            elif existe_en_usuario and not alta:
                return que_identificador
            #Si el identificador existe en la lista de plantas potabilizadoras y en la lista de plantas potabilizadoras de los usuarios y se quiere dar de alta indicando que ya está en uso
            elif existe_en_usuario and alta:
                print("Este identificador ya está en uso para una planta potabilizadora. Introduce un identificador nuevo.")
            #Si el identificador existe en la lista de plantas potabilizadoras y no en la lista de plantas potabilizadoras de los usuarios y se quiere modificar indicando que no hay registros para esa planta
            elif not existe_en_usuario and not alta:
                print("No hay registros de uso para este identificador. Introduce un identificador que ya esté en uso.")
    except:
        print("Error al solicitar el identificador.")
        menu_principal.menu_principal()

# Da de alta una planta potabilizadora
def alta_planta():
    try:
        if variables.plantas_potabilizadoras_usuarios != []:
            print("\n¿Quieres ver el listado de plantas potabilizadoras ya introducidas?")
            print("1) Sí")
            print("2) No")
            if input("Elige una opción (1-2): ") == "1":
                mostrar_plantas()
        que_identificador = solicitar_identificador(alta=True)
        # Solicita la eficiencia de la planta potabilizadora
        eficiencia = input(
            "Ingresa la eficiencia de la planta potabilizadora (Alta, Media, Baja): "
        ).title()
        # Comprueba si la eficiencia es válida si no es válida pide que se introduzca una eficiencia válida
        while eficiencia not in variables.eficiencia:
            print("Por favor, introduce una eficiencia valida.")
            eficiencia = input("Ingresa la eficiencia: ").title()
        # Solicita la cantidad de litros que potabiliza la planta potabilizadora y comprueba que sea mayor a 0 si no es mayor a 0 pide que se introduzca una cantidad mayor a 0
        litros = int(input("Cantidad de litros que potabiliza la planta: "))
        while int(litros) <= 0:
            print("Introduce una cifra valida mayor a 0")
            litros = input("Cantidad de litros que potabiliza la planta: ")
        # Añade la planta potabilizadora a la lista de plantas potabilizadoras de los usuarios
        variables.plantas_potabilizadoras_usuarios.append(
            {
                "Id": que_identificador,
                "Eficiencia": eficiencia,
                "Litros": int(litros),
            }
        )
        print("Planta añadida correctamente.")
    except:
        print("Error al añadir la planta.")
        menu_principal.menu_principal()
# Modifica una planta potabilizadora
def modificar_planta():
    try:
        # Muestra las plantas potabilizadoras disponibles
        mostrar_plantas()
        que_identificador = solicitar_identificador(alta=False)
        print("\n¿Quieres modificar la eficiencia, los litros o dar de baja?")
        print("1) Eficiencia")
        print("2) Litros")
        print("3) Dar de baja")
        que_modifica = input("Elige una opción (1-2-3): ")
        # Comprueba si la opción es válida si no es válida pide que se introduzca una opción válida
        while que_modifica not in ["1", "2", "3"]:
            print("Opción no válida. Elige una opción válida.")
            print("\n¿Quieres modificar la calidad, los litros o dar de baja?")
            print("1) Calidad")
            print("2) Litros")
            print("3) Dar de baja")        
            que_modifica = input("Elige una opción (1-2-3): ")
        # Si la opción es dar de baja elimina la planta potabilizadora
        if que_modifica == "3":
            variables.plantas_potabilizadoras_usuarios = [
                planta
                for planta in variables.plantas_potabilizadoras_usuarios
                if planta["Id"] != que_identificador
            ]
            print("Planta eliminada correctamente.")
            return
        # Si la opción es modificar la eficiencia solicita la nueva eficiencia y comprueba si es válida si no es válida pide que se introduzca una eficiencia válida
        if que_modifica == "1":
            nueva_info = input("Introduce la nueva eficiencia " + str(variables.eficiencia) + ": ").title()
            if nueva_info not in variables.eficiencia:
                print("Eficiencia no válida.")
                while nueva_info not in variables.eficiencia:
                    print("Eficiencia no válida. Introduce una eficiencia válida.")
                    nueva_info = input("Introduce la nueva eficiencia " + str(variables.eficiencia) + ": ").title()
            for planta in variables.plantas_potabilizadoras_usuarios:
                if planta["Id"] == que_identificador:
                    planta["Eficiencia"] = nueva_info
                    print("Información actualizada correctamente.")
                else:
                    continue
        # Si la opción es modificar los litros solicita la nueva cantidad de litros y comprueba si es mayor a 0 si no es mayor a 0 pide que se introduzca una cantidad mayor a 0
        if que_modifica == "2":
            nueva_info = input("Introduce la nueva cantidad de litros: ")
            if int(nueva_info) <= 0:
                print("Introduce una cifra mayor a 0.")
                while int(nueva_info) <= 0:
                    print("Introduce una cifra mayor a 0.")
                    nueva_info = input("Introduce la nueva cantidad de litros: ")
            for planta in variables.plantas_potabilizadoras_usuarios:
                if planta["Id"] == que_identificador:
                    planta["Litros"] = nueva_info
                    print("Información actualizada correctamente.")
                else:
                    continue
    except:
        print("Error al modificar la planta.")
        menu_principal.menu_principal()

# Menú de plantas potabilizadoras
def menu_planta_potabilizadora():
    try:
        # Si no hay plantas potabilizadoras disponibles muestra el menú de alta
        while True:
            if variables.plantas_potabilizadoras_usuarios == []:
                print("\nMenú de Plantas Potabilizadoras")
                print("1) Dar de alta una planta potabilizadora")
                print("2) Salir al menú principal")
                
                opcion = input("Elige una opción (1-2): ")
                if opcion == "1":
                    alta_planta()
                elif opcion == "2":
                    return  # Regresa al menú principal
                else:
                    print("Por favor, selecciona una opción válida.")
            # Si hay plantas potabilizadoras disponibles muestra el menú completo
            else:
                print("\nMenú de Plantas Potabilizadoras")
                print("1) Dar de alta una planta potabilizadora")
                print("2) Modificar una planta potabilizadora")
                print("3) Salir al menú principal")
                opcion = input("Elige una opción (1-2-3): ")
                if opcion == "1":
                    alta_planta()
                elif opcion == "2":
                    modificar_planta()
                elif opcion == "3":
                    return  # Regresa al menú principal
                else:
                    print("Por favor, selecciona una opción válida.")
    except:
        print("Error al mostrar el menú de plantas potabilizadoras.")
        menu_principal.menu_principal()


# Integración con el menú principal si es llamado directamente
if __name__ == "__main__":
    menu_planta_potabilizadora()
    menu_principal.menu_principal()

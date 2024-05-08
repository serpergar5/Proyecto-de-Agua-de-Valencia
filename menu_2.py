import variables
import menu_principal


def mostrar_plantas():
    try:
        print(
            "\nListado de plantas potabilizadoras disponibles: "
            + ", ".join(variables.plantas_potabilizadoras)
            + ": "
        )
    except:
        print("Error al mostrar las plantas potabilizadoras.")
        menu_principal.menu_principal()

def solicitar_identificador(alta):
    try:
        while True:
            que_identificador = input("Introduce el identificador de la planta potabilizadora: ").upper()
            existe_en_registros = any(
                planta == que_identificador for planta in variables.plantas_potabilizadoras
            )
            existe_en_usuario = any(
                planta_usuarios["Id"] == que_identificador
                for planta_usuarios in variables.plantas_potabilizadoras_usuarios
            )
            if not existe_en_registros:
                print("Identificador no encontrado. Intente de nuevo con un identificador de la lista de plantas potabilizadoras disponibles.")
            elif existe_en_registros and not existe_en_usuario and alta:
                return que_identificador
            elif existe_en_registros and existe_en_usuario and not alta:
                return que_identificador
            elif existe_en_registros and existe_en_usuario and alta:
                print("Este identificador ya está en uso para una planta potabilizadora. Introduce un identificador nuevo.")
            elif existe_en_registros and not existe_en_usuario and not alta:
                print("No hay registros de uso para este identificador. Introduce un identificador que ya esté en uso.")
    except:
        print("Error al solicitar el identificador.")
        menu_principal.menu_principal()

def alta_planta():
    try:
        print("\n¿Quieres ver el listado de plantas potabilizadoras disponibles?")
        print("1) Sí")
        print("2) No")
        if input("Elige una opción (1-2): ") == "1":
            mostrar_plantas()
        que_identificador = solicitar_identificador(alta=True)

        eficiencia = input(
            "Ingresa la eficiencia de la planta potabilizadora (Alta, Media, Baja): "
        ).title()
        while eficiencia not in variables.eficiencia:
            print("Por favor, introduce una eficiencia valida.")
            eficiencia = input("Ingresa la eficiencia: ").title()

        litros = int(input("Cantidad de litros que potabiliza la planta: "))
        while int(litros) <= 0:
            print("Introduce una cifra valida mayor a 0")
            litros = input("Cantidad de litros que potabiliza la planta: ")

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

def modificar_planta():
    try:
        mostrar_plantas()
        que_identificador = solicitar_identificador(alta=False)
        print("\n¿Quieres modificar la eficiencia, los litros o dar de baja?")
        print("1) Eficiencia")
        print("2) Litros")
        print("3) Dar de baja")
        que_modifica = input("Elige una opción (1-2-3): ")

        while que_modifica not in ["1", "2", "3"]:
            print("Opción no válida. Elige una opción válida.")
            print("\n¿Quieres modificar la calidad, los litros o dar de baja?")
            print("1) Calidad")
            print("2) Litros")
            print("3) Dar de baja")        
            que_modifica = input("Elige una opción (1-2-3): ")

        if que_modifica == "3":
            variables.plantas_potabilizadoras_usuarios = [
                planta
                for planta in variables.plantas_potabilizadoras_usuarios
                if planta["Id"] != que_identificador
            ]
            print("Planta eliminada correctamente.")
            return

        if que_modifica == "1":
            nueva_info = input("Introduce la nueva eficiencia " + str(variables.eficiencia) + ": ").title()
            if nueva_info not in variables.eficiencia:
                print("Eficiencia no válida.")
                return
            for planta in variables.plantas_potabilizadoras_usuarios:
                if planta["Id"] == que_identificador:
                    planta["Eficiencia"] = nueva_info
                    print("Información actualizada correctamente.")
                else:
                    continue
            
        if que_modifica == "2":
            nueva_info = input("Introduce la nueva cantidad de litros: ")
            if int(nueva_info) <= 0:
                print("Introduce una cifra mayor a 0.")
                return
            for planta in variables.plantas_potabilizadoras_usuarios:
                if planta["Id"] == que_identificador:
                    planta["Litros"] = nueva_info
                    print("Información actualizada correctamente.")
                else:
                    continue
    except:
        print("Error al modificar la planta.")
        menu_principal.menu_principal()

def menu_planta_potabilizadora():
    try:
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

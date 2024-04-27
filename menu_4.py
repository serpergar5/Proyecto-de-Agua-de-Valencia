import variables
import menu_principal


def fuente_planta():
    while True:
        if i is None:
            fuentes_hidricas_interconectadas_imprimir = []
            planta_potabilizadora_interconectadas_imprimir = []
            for e in variables.fuentes_hidricas_usuarios:
                for i in variables.plantas_potabilizadoras_usuarios:
                    if e["Litros"]<=i["Litros"]:
                        eficiencia_porcentaje = (1-(e["Uso"]))+(1-(i["Uso"]))
                        if eficiencia_porcentaje == 2:
                            eficiencia_porcentaje = 1

                        variables.fuentes_hidricas_intercontectables.append(
                            {
                                "Fuente hídrica": e["Fuente hídrica"],
                                "Planta potabilizadora": i["Planta potabilizadora"],
                                "Litros ocupados": e["Litros"],
                                "Litros potabilizados": (eficiencia_porcentaje * e["Litros"]),
                            }
                        )
                        if e["Fuente hídrica"] not in fuentes_hidricas_interconectadas_imprimir:
                            fuentes_hidricas_interconectadas_imprimir.append(e["Fuente hídrica"])
                        if i["Planta potabilizadora"] not in planta_potabilizadora_interconectadas_imprimir:
                            fuentes_hidricas_interconectadas_imprimir.append(i["Planta potabilizadora"])
                    else:
                        continue
            i == 0
                
        if i == 0:
            que_identificador = input("Elige un identificador para una de las siguientes fuentes hídricas, " + fuentes_hidricas_interconectadas_imprimir + ": ").upper()
            comprobar_si_existe_fuente = False

            comprobar_si_existe_fuente == any(
                dato_usuarios["Fuente hídrica"] == que_identificador
                for dato_usuarios in variables.fuentes_hidricas_intercontectables
                )
            if comprobar_si_existe_fuente == True:
                i = 1
            else:
                print("Introduce una fuente hídrica valida.")
                
            if i == 1:
                planta_potabilizadora_usuario = str(input("Elige un identificador para una de las siguientes plantas potabilizadoras: " + planta_potabilizadora_interconectadas_imprimir + ": "))
                comprobar_si_existe_planta = False

                comprobar_si_existe_planta = any(
                    dato_usuarios["Planta potabilizadora"] == planta_potabilizadora_usuario
                    for dato_usuarios in variables.fuentes_hidricas_intercontectables
                )
                if comprobar_si_existe_planta == True:
                    i = 2
                else: print("Introduce una planta potabilizadora valida.")
                
                if i == 2:
                    porcentaje = int(input("Elige el porcentaje de interconexión: "))
                    dato_usuarios["Porcentaje"] = porcentaje
                    for dato_usuarios in variables.fuentes_hidricas_intercontectables:
                        if (
                            dato_usuarios["Fuente hídrica"] == que_identificador
                            and dato_usuarios["Planta potabilizadora"]
                            == planta_potabilizadora_usuario
                        ):
                            dato_usuarios["Porcentaje"] = porcentaje
                            break

                    nombre_interconexión = que_identificador + "-" + planta_potabilizadora_usuario + "-1"

                    variables.fuentes_hidricas_planta_potabilizadora.append(
                            {
                                "Fuente hídrica": que_identificador,
                                "Planta potabilizadora": planta_potabilizadora_usuario,
                                "Porcentaje interconexión": porcentaje,
                                "Litros ocupados": e["Litros"],
                                "Litros potabilizados": (eficiencia_porcentaje * e["Litros"]),
                                "id": nombre_interconexión
                            }
                        )



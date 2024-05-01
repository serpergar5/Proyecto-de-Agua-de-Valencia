import variables


def listar_recursos_con_capacidad(recursos):
    disponibles = {
        nombre: recurso for nombre, recurso in recursos.items() if recurso["Uso"] < 100
    }
    for nombre, recurso in disponibles.items():
        print(f"{nombre} - Uso actual: {recurso['Uso']}%")


def seleccionar_recurso(recursos, tipo):
    listar_recursos_con_capacidad(recursos)
    eleccion = input(f"Selecciona un {tipo} de la lista: ")
    return recursos.get(eleccion, None)


def conectar_recursos(origen, destino, capacidad):
    if origen["Uso"] + capacidad > 100:
        print(
            f"Capacidad de interconexión excede el límite disponible para {origen['nombre']}."
        )
        capacidad = 100 - origen["Uso"]
        print(f"Solo se puede asignar hasta {capacidad}% de capacidad.")
    origen["Uso"] += capacidad
    destino["Uso"] += capacidad
    print(
        f"Conectado {origen['nombre']} con {destino['nombre']} al {capacidad}% de su capacidad."
    )
    return f"{origen['nombre']}-{destino['nombre']}-{capacidad}"


def alta_interconexion():
    tipo_recurso = input(
        "¿Quieres interconectar una 'Fuente hídrica' o una 'Planta Potabilizadora'? "
    ).title()
    if tipo_recurso == "Fuente Hídrica":
        origen = seleccionar_recurso(variables.fuentes_hidricas_usuarios, "fuente")
        destino = seleccionar_recurso(
            variables.plantas_potabilizadoras_usuarios, "planta potabilizadora"
        )
    else:
        origen = seleccionar_recurso(
            variables.plantas_potabilizadoras_usuarios, "planta potabilizadora"
        )
        destino = seleccionar_recurso(
            variables.centros_distribucion, "centro de distribución"
        )

    if origen and destino:
        capacidad = int(input("Introduce el porcentaje de interconexión (%): "))
        id_interconexion = conectar_recursos(origen, destino, capacidad)
        print("Interconexión realizada con éxito:", id_interconexion)
    else:
        print(
            "Error: uno de los recursos seleccionados no es válido o no está disponible."
        )


# Llamada a la función de alto nivel para iniciar el proceso
alta_interconexion()

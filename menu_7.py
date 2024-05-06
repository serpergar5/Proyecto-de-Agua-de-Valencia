import csv
import variables
import menu_principal

def cargar_datos():
    ficheros = {
        "Entradas/fh.csv": (variables.fuentes_hidricas_usuarios, ['Id', 'Calidad', 'Litros']),
        "Entradas/pb.csv": (variables.plantas_potabilizadoras_usuarios, ['Id', 'Eficiencia', 'Litros']),
        "Entradas/cd.csv": (variables.centros_distribucion_usuarios, ['Id', 'Capacidad máxima', 'Reserva actual', 'Consumo diario']),
        "Entradas/fh-pb.csv": (variables.interconexiones_fh, ['Id', 'Origen', 'Destino', 'Porcentaje']),
        "Entradas/pb-cd.csv": (variables.interconexiones_pb, ['Id', 'Origen', 'Destino', 'Porcentaje'])
    }

    for fichero, (lista, campos) in ficheros.items():
        try:
            with open(fichero, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                if reader.fieldnames != campos:
                    raise ValueError("El archivo " + fichero + " no tiene las columnas esperadas: " + campos)
                lista.clear()
                lista.extend(row for row in reader)
            print("Datos cargados correctamente desde " + fichero + ".")
        except FileNotFoundError:
            print("Archivo " + fichero +" no encontrado. Asegúrate de que el archivo exista.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("Error al cargar los datos de " + fichero + ":" + str(e))

def guardar_datos():
    archivos = {
        'fuente': ('Salidas/fuentes.csv', variables.fuentes_hidricas_usuarios),
        'planta': ('Salidas/plantas.csv', variables.plantas_potabilizadoras_usuarios),
        'centro': ('Salidas/centros.csv', variables.centros_distribucion_usuarios),
        'interconexion_fh': ('Salidas/interconexiones_fh.csv', variables.interconexiones_fh),
        'interconexion_pb': ('Salidas/interconexiones_pb.csv', variables.interconexiones_pb)
    }

    for tipo, (archivo, lista) in archivos.items():
        fieldnames = list(lista[0].keys()) if lista else []
        try:
            with open(archivo, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(lista)
            print("Datos de " + tipo + " guardados correctamente en " + archivo + ".")
        except Exception as e:
            print("Error al guardar los datos de " + tipo + " en "+ archivo + ":" + str(e))


def menu_ficheros():
    while True:
        print("\nMenú de Gestión de Ficheros")
        print("1) Cargar datos desde un fichero")
        print("2) Guardar datos en un fichero")
        print("3) Salir al menú principal")

        opcion = input("Elige una opción (1-2-3): ")

        if opcion == '1':
            cargar_datos()
        elif opcion == '2':
            guardar_datos()
        elif opcion == '3':
            print("Saliendo del menú de ficheros.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu_ficheros()
    menu_principal.menu_principal()
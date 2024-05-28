import csv
import variables
import menu_principal

# Carga los datos de los ficheros en las listas de variables. Si no se encuentra un fichero, muestra un mensaje de error. Si el fichero no tiene las columnas esperadas, muestra un mensaje de error. Si hay un error al cargar los datos, muestra un mensaje de error. Si todo va bien, muestra un mensaje de éxito. 
def cargar_datos():
    try:
        rutafh = str(input("Introduce el nombre del fichero de fuentes hídricas: "))
        rutapb = str(input("Introduce el nombre del fichero de plantas potabilizadoras: "))
        rutacd = str(input("Introduce el nombre del fichero de centros de distribución: "))
        rutafhpb = str(input("Introduce el nombre del fichero de interconexiones de fuentes hídricas a plantas potabilizadoras: "))
        rutapbcd = str(input("Introduce el nombre del fichero de interconexiones de plantas potabilizadoras a centros de distribución: "))
        # Diccionario con los ficheros y las listas a las que se cargarán los datos de los ficheros y las columnas esperadas en los ficheros
        ficheros = {
            "Entradas/"+rutafh+".csv": (variables.fuentes_hidricas_usuarios, ['Id', 'Calidad', 'Litros']),
            "Entradas/"+rutapb+".csv": (variables.plantas_potabilizadoras_usuarios, ['Id', 'Eficiencia', 'Litros']),
            "Entradas/"+rutacd+".csv": (variables.centros_distribucion_usuarios, ['Id', 'Capacidad máxima', 'Reserva actual', 'Consumo diario']),
            "Entradas/"+rutafhpb+".csv": (variables.interconexiones_fh, ['Id', 'Origen', 'Destino', 'Porcentaje']),
            "Entradas/"+rutapbcd+".csv": (variables.interconexiones_pb, ['Id', 'Origen', 'Destino', 'Porcentaje'])
        }
        # Iteramos sobre los ficheros y las listas y columnas correspondientes en el diccionario 
        for fichero, (lista, campos) in ficheros.items():
            try:
                # Abrimos el fichero en modo lectura y leemos los datos en un diccionario
                with open(fichero, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    # Si las columnas del fichero no son las esperadas, muestra un mensaje de error
                    if reader.fieldnames != campos:
                        raise ValueError("El archivo " + fichero + " no tiene las columnas esperadas: " + campos)
                    # Si las columnas del fichero son las esperadas, cargamos los datos en la lista correspondiente y mostramos un mensaje de éxito
                    lista.clear()
                    lista.extend(row for row in reader)
                print("Datos cargados correctamente desde " + fichero + ".")
            except FileNotFoundError:
                print("Archivo " + fichero +" no encontrado. Asegúrate de que el archivo exista.")
            except ValueError as ve:
                print(ve)
            except Exception as e:
                print("Error al cargar los datos de " + fichero + ":" + str(e))
    except:
        print("Error al cargar los datos.")
        menu_principal.menu_principal()

# Guarda los datos de las listas en los ficheros. Si hay un error al guardar los datos, muestra un mensaje de error. Si todo va bien, muestra un mensaje de éxito.
def guardar_datos():
    try:
        rutafh = str(input("Introduce el nombre del fichero de fuentes hídricas: "))
        rutapb = str(input("Introduce el nombre del fichero de plantas potabilizadoras: "))
        rutacd = str(input("Introduce el nombre del fichero de centros de distribución: "))
        rutafhpb = str(input("Introduce el nombre del fichero de interconexiones de fuentes hídricas a plantas potabilizadoras: "))
        rutapbcd = str(input("Introduce el nombre del fichero de interconexiones de plantas potabilizadoras a centros de distribución: "))
        # Diccionario con los ficheros y las listas de las que se guardarán los datos en los ficheros
        archivos = {
            'fuente': ('Salidas/'+rutafh+'.csv', variables.fuentes_hidricas_usuarios),
            'planta': ('Salidas/'+rutapb+'.csv', variables.plantas_potabilizadoras_usuarios),
            'centro': ('Salidas/'+rutacd+'.csv', variables.centros_distribucion_usuarios),
            'interconexion_fh': ('Salidas/'+rutafhpb+'.csv', variables.interconexiones_fh),
            'interconexion_pb': ('Salidas/'+rutapbcd+'.csv', variables.interconexiones_pb)
        }
        # Iteramos sobre los archivos y las listas correspondientes en el diccionario
        for tipo, (archivo, lista) in archivos.items():
            fieldnames = list(lista[0].keys()) if lista else []
            with open(archivo, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(lista)
            print("Datos de " + tipo + " guardados correctamente en " + archivo + ".")
    except Exception as e:
        print("Error al guardar los datos de " + tipo + " en "+ archivo + ":" + str(e))
        menu_principal.menu_principal()

# Menú de gestión de ficheros que permite cargar y guardar los datos de los ficheros 
def menu_ficheros():
    try:
        # Muestra el menú de gestión de ficheros y procesa la selección del usuario
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
    except:
        print("Error en el menú de ficheros.")
        menu_principal.menu_principal()

if __name__ == "__main__":
    menu_ficheros()
    menu_principal.menu_principal()
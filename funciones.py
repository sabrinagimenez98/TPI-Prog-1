import csv, os
from utils import quitar_tildes 

RUTA_ARCHIVO = "ARCHIVO_PAISES\\paises.csv"

# --------------------------
# FUNCIONES PROGRAMA
# -------------------------

# Función para crear archivo si no existe
def inicializar_archivo():
    try:
        if not os.path.exists(RUTA_ARCHIVO):
            with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
                # nombre de las Claves/Encabezados
                encabezados = ["nombre", "poblacion", "superficie", "continente"]

                # Crea una lista de diccionarios y toma la primer linea/fila como encabezados como (key), y los demas como (value)
                escritor = csv.DictWriter(archivo, fieldnames=encabezados)

                # escribe los encabezados en el archivo
                escritor.writeheader()
            print(f" Archivo '{RUTA_ARCHIVO}' creado correctamente con los encabezados.")
        else:
            print(f" El archivo '{RUTA_ARCHIVO}' ya existe. No se requiere inicializar.")

    except IOError as e:
        print(f" Error crítico al crear/acceder al archivo: {e}")
    except Exception as e:
        print(f" Ocurrió un error inesperado al inicializar: {e}")

# --------------------------
# FUNCIONES MENU
# --------------------------

def mostrar_paises():
    print("\n---LISTADO DE PAÍSES REGISTRADOS---")
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            # lee el contenido del archivo como lista de diccionarios
            contenido = csv.DictReader(archivo)
            contenido = list(contenido)

            if not contenido:
                print("No hay países registrados en el archivo.")
                return

            # Encabezado con ancho fijo
            print("-" * 80)
            print(f"{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)' :<17} | {'Continente':<15}")
            print("-" * 80)

            contenido_valido = []
            errores_formato = 0

            # Países: Validación de tipos y manejo de errores de conversión por fila
            for i, fila in enumerate(contenido):
                try:
                    nombre = fila['nombre']
                    # Validamos y convertimos los tipos antes de operar/mostrar
                    poblacion = int(fila['poblacion'])
                    superficie = float(fila['superficie'])
                    continente = fila['continente']

                    # Se añade una validación extra para números no negativos
                    if poblacion < 0 or superficie < 0:
                         print(f"Fila {i+2}: Datos numéricos inválidos (negativos) para '{nombre}'. Se omitirá.")
                         errores_formato += 1
                         continue

                    print(f"{nombre:<20} | {poblacion:>15} | {superficie:>17.2f} | {continente:<15}")

                    contenido_valido.append(fila)

                # Captura ValueError si 'poblacion' o 'superficie' no son números válidos
                except ValueError:
                    print(f"Error en la Fila {i+2} (País: {fila.get('nombre', 'Desconocido')}): Error de formato en Población o Superficie. Se omitirá.")
                    errores_formato += 1
                # Captura KeyError si faltan encabezados/columnas
                except KeyError as e:
                    print(f"Error en la Fila {i+2}: Falta la columna necesaria: {e}. Se omitirá.")
                    errores_formato += 1

            print("-" * 80)
            
            # Sobrescribo el csv original SÓLO si hubo errores de formato para 'limpiar' el archivo.
            if errores_formato > 0:
                print(f"Se encontraron y limpiaron {errores_formato} filas con errores de formato del archivo.")
                if contenido_valido:
                    with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo_out:
                        encabezado = ["nombre", "poblacion", "superficie", "continente"]
                        escritor = csv.DictWriter(archivo_out, fieldnames=encabezado)
                        escritor.writeheader()
                        escritor.writerows(contenido_valido)
                    print("Archivo actualizado correctamente con solo datos válidos.")
                else:
                    print("El archivo quedó vacío después de la limpieza.")
                    
            if not contenido_valido and not contenido: # Caso donde se limpia el archivo pero no queda nada
                print("No quedaron países válidos para mostrar.")
            elif contenido_valido:
                 print(f"Mostrados {len(contenido_valido)} países sin problemas.")
                

    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al leer el archivo CSV. Verifique la estructura del archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al mostrar los países: {e}")

def buscar_pais():
    print("\n---BÚSQUEDA DE PAÍS---")
    pais_buscar = input("➡️ Ingrese el nombre del país que desea buscar: ").strip()

    # 1. Validación de entrada (Logs detallados)
    if not pais_buscar:
        print("Error: Entrada vacía. Inténtelo de nuevo.")
        return

    # Validar que no contenga solo números (aunque podría ser un nombre válido, es una buena práctica)
    if pais_buscar.isdigit():
        print("Error: El nombre del país no puede ser un valor puramente numérico. Inténtelo de nuevo.")
        return

    # Quito las tildes al pais ingresado para la comparacion.
    pais_sin_tildes = quitar_tildes(pais_buscar.lower())

    encontrado = False

    # 2. Manejo de errores de archivo
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    # Quito las tildes del pais que está dentro del CSV
                    nombre_csv = fila["nombre"]
                    nombre_sin_tildes = quitar_tildes(nombre_csv.lower())

                    # Comparacion
                    if nombre_sin_tildes == pais_sin_tildes:
                        print(f"\n{'=' * 40}")
                        print(f"País Encontrado: **{nombre_csv}**")
                        print(f"| Nombre: {nombre_csv}")
                        # Se añade try/except para la conversión de tipos al mostrar, si fuera necesario
                        try:
                             print(f"| Población: {int(fila['poblacion']):,}")
                             print(f"| Superficie: {float(fila['superficie']):,.2f} km²")
                        except ValueError:
                             print("| Población/Superficie: Datos no numéricos (¡Advertencia de formato!)")
                        print(f"| Continente: {fila['continente']}")
                        print(f"{'=' * 40}")
                        encontrado = True
                        break
                except KeyError:
                     # Error interno del CSV (faltan columnas)
                    print(f"Advertencia: Fila con formato incompleto omitida.")
                    continue
            
            # Log de error si no se encuentra
            if not encontrado:
                print(f"Error: El país '{pais_buscar}' no se encuentra en el registro.")

    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Creando uno nuevo....")
        inicializar_archivo()
    except csv.Error:
        print("Error al procesar el archivo CSV durante la búsqueda.")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la búsqueda: {e}")


def agregar_pais():
    print("\n---AGREGAR NUEVO PAÍS---")
    # Se estandarizan los continentes para la validación
    continentes_validos = ["america", "europa", "asia", "africa", "oceania", "antartida"]

    # 1. Entrada y validación de nombre de país (Log de error)
    nuevo_nombre = input("Ingrese el nombre del país a ingresar: ").strip()
    if not nuevo_nombre:
        print("Error: El nombre del país no puede estar vacío. Inténtelo de nuevo.")
        return
    if nuevo_nombre.isdigit():
        print("Error: El nombre del país no puede ser un valor puramente numérico. Inténtelo de nuevo.")
        return
    
    # 2. Verificación de existencia del país
    try:
        # Se verifica la existencia dentro del archivo antes de pedir más datos
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)

            # Verificación para saber si existe dentro del csv
            nombre_a_comparar = quitar_tildes(nuevo_nombre.lower())
            for pais in paises:
                if quitar_tildes(pais.get("nombre", "").lower()) == nombre_a_comparar:
                    print(f"Error: El país '{nuevo_nombre.capitalize()}' ya se encuentra dentro del sistema.")
                    return
    except FileNotFoundError:
        # Si no existe, se inicializa el archivo, pero se continúa para permitir agregar el primer país.
        print(f"Advertencia: Archivo no encontrado. Se creará uno nuevo al guardar.")
        pass # Continúa con la entrada de datos si el archivo no existe
    except csv.Error:
        print("Error al procesar el archivo CSV durante la verificación de duplicados.")
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado al verificar el país: {e}")
        return
    
    # 3. Entrada y validación de población (Log de error y try/except implícito en isdigit)
    nuevo_poblacion_str = input("Ingrese la población del país (entero): ").strip()
    try:
        if not nuevo_poblacion_str.isdigit():
             raise ValueError("No es un número entero positivo.")
        
        nuevo_poblacion = int(nuevo_poblacion_str)
        if nuevo_poblacion < 0:
            raise ValueError("No puede ser negativo.")
            
    except ValueError as e:
        print(f"Error de Validación en Población: Debe ser un número entero positivo. {e}. Inténtelo de nuevo.")
        return

    # 4. Entrada y validación de superficie (Log de error y try/except explícito para float)
    nuevo_superficie_str = input("➡️ Ingrese la superficie del país (decimal, ej: 123.45): ").strip()
    try:
        # Reemplazo de coma por punto si se usa en la entrada (común en español)
        nuevo_superficie_str = nuevo_superficie_str.replace(',', '.')
        nuevo_superficie = float(nuevo_superficie_str)
        
        if nuevo_superficie < 0:
            raise ValueError("No puede ser negativo.")

    except ValueError:
        print("Error de Validación en Superficie: Debe ser un número decimal positivo válido. Inténtelo de nuevo.")
        return

    # 5. Entrada y validación de continente (Log de error)
    nuevo_continente = input("➡️ Ingrese el continente del país: ").strip().lower()
    if nuevo_continente not in continentes_validos:
        print(f"Error: Continente inválido. Los válidos son: {', '.join(continentes_validos)}. Inténtelo de nuevo.")
        return

    # Creación de la fila del país
    nuevo_pais = {
        "nombre": nuevo_nombre.capitalize(),
        "poblacion": str(nuevo_poblacion), # Se guarda como string
        "superficie": f"{nuevo_superficie:.2f}", # Se guarda como string con 2 decimales
        "continente": nuevo_continente.capitalize()}

    # 6. Escritura en el archivo con try/except para el I/O
    try:
        # El modo 'a' (append) y newline="" evitan problemas de líneas en blanco
        archivo_existe = os.path.exists(RUTA_ARCHIVO)
        if not archivo_existe:
             inicializar_archivo() # Asegura que al menos el archivo se cree con encabezados

        with open(RUTA_ARCHIVO, "a", encoding="utf-8", newline="") as archivo:
            encabezados = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=encabezados)
            escritor.writerow(nuevo_pais)

        print(f"\nPaís **{nuevo_nombre.capitalize()}** agregado correctamente.")

    except IOError as e:
        print(f" Error de I/O al escribir en el archivo: {e}")
    except csv.Error:
        print(" Error al escribir la fila en el archivo CSV.")
    except Exception as e:
        print(f" Ocurrió un error inesperado al guardar el país: {e}")


def eliminar_pais():
    print("\n--- ELIMINAR PAÍS  ---")
    pais_eliminar = input("Ingrese el país que desea eliminar: ").strip()

    # 1. Validación de entrada (Log de error)
    if not pais_eliminar:
        print(" Error: Entrada vacía. Inténtelo de nuevo.")
        return

    # 2. Existencia de archivo (Manejo de errores)
    if not os.path.exists(RUTA_ARCHIVO):
        print(f" Error: El archivo '{RUTA_ARCHIVO}' no existe. No hay países para eliminar.")
        inicializar_archivo()
        return

    # Normalización del nombre a eliminar para comparación
    nombre_a_eliminar = quitar_tildes(pais_eliminar.lower())

    # 3. Lectura y modificación del archivo con try/except
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)

            encontrado = False
            paises_modificado = []

            # Búsqueda del país ingresado por el usuario
            for pais in paises:
                # Se utiliza .get() para evitar KeyError si la fila está incompleta
                if quitar_tildes(pais.get("nombre", "").lower()) == nombre_a_eliminar:
                    encontrado = True
                else:
                    paises_modificado.append(pais)

        # 4. Escritura del nuevo archivo (sin el país eliminado)
        if encontrado:
            # Se usa el modo 'w' (write) para sobrescribir y eliminar el país
            with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo_out:
                encabezado = ["nombre", "poblacion", "superficie", "continente"]
                escritor = csv.DictWriter(archivo_out, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(paises_modificado)

            # Log de éxito
            print(f"\nPaís **{pais_eliminar.capitalize()}** eliminado con éxito.")
            if not paises_modificado:
                 print("El archivo de países ahora está vacío.")

        else:
            # Log de error (no encontrado)
            print(f"Error: El país '{pais_eliminar.capitalize()}' no se encuentra en el sistema.")

    except IOError as e:
        print(f"Error de I/O al leer/escribir el archivo: {e}")
    except csv.Error:
        print("Error al procesar el archivo CSV. Verifique el formato.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al intentar eliminar el país: {e}")

from funciones import RUTA_ARCHIVO, inicializar_archivo
import csv
import os
#------------------------------------------
# ORDENAMIENTOS
#------------------------------------------

def buscar_nombre(pais):
    """Función clave para ordenar por nombre (insensible a mayúsculas/minúsculas)."""
    # Manejo de KeyError si la columna 'nombre' falta (aunque es poco probable)
    return pais.get("nombre", "").lower() 

def ordenamiento_nombre():
    print("\n---ORDENAR POR NOMBRE (ALFABÉTICO)---")
    
    # 1. Manejo de error de archivo
    if not os.path.exists(RUTA_ARCHIVO):
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Inicializando...")
        inicializar_archivo()
        return

    try:
        # Apertura de archivo para lectura
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo_in:
            lector = csv.DictReader(archivo_in)
            paises = list(lector)
            
            if not paises:
                print("El archivo está vacío. No hay países para ordenar.")
                return
            
            paises_ordenados = sorted(paises, key=buscar_nombre)

        # 2. Escritura del nuevo archivo ordenado
        with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo_out:
            encabezado = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo_out, fieldnames=encabezado)
            escritor.writeheader()
            escritor.writerows(paises_ordenados)
            
        # 3. Log de éxito
        print(f"\nPaíses ordenados correctamente por nombre (A-Z) y guardados en '{RUTA_ARCHIVO}'.")
            
    except FileNotFoundError:
        # Este error debería ser capturado por la verificación inicial, pero se mantiene por seguridad
        print("Error: Archivo no encontrado. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al procesar el archivo CSV durante el ordenamiento por nombre.")

# ------------------------------------------------------------------------
# Lógica para Ordenamiento por Población
# ------------------------------------------------------------------------

def obtener_poblacion(pais):
    try:
        # Se asegura que la población sea un entero y no sea negativa.
        poblacion = int(pais["poblacion"])
        if poblacion < 0:
            return -1 # Valor negativo se ordena antes si es descendente
        return poblacion
    except (ValueError, KeyError):
        # Si no es un número o la clave falta, devuelve 0 para agrupar los inválidos
        # o un valor muy grande/pequeño según el contexto. Aquí devolvemos 0.
        print(f"Advertencia: Población inválida ('{pais.get('poblacion')}') para '{pais.get('nombre', 'país desconocido')}' ignorada o tratada como 0.")
        return 0

def ordenamiento_poblacion(opcion):
    
    # 1. Manejo de error de archivo
    if not os.path.exists(RUTA_ARCHIVO):
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Inicializando...")
        inicializar_archivo()
        return
    
    # Definir el modo para el mensaje de éxito
    modo = "Ascendente (Menor a Mayor)" if opcion == "a" else "Descendente (Mayor a Menor)"

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo_in:
            lector = csv.DictReader(archivo_in)
            paises = list(lector)
            
            if not paises:
                print("El archivo está vacío. No hay países para ordenar.")
                return
            
            # Ordenamiento Ascendente y Descendente (a/d)
            # El manejo de errores de tipo ocurre dentro de la función 'obtener_poblacion'
            if opcion == "a":
                # Ordena ascendentemente. 'obtener_poblacion' devuelve 0 o el valor real.
                ordenados_poblacion = sorted(paises, key=obtener_poblacion)
            
            elif opcion == "d":
                # Ordena descendentemente.
                ordenados_poblacion = sorted(paises, key=obtener_poblacion, reverse=True)
            
            else:
                 print("Error de lógica: Opción de ordenamiento inválida recibida.")
                 return

        # 2. Escritura del nuevo archivo ordenado
        with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo_out:
            encabezado = ["nombre","poblacion","superficie","continente"]
            escritor = csv.DictWriter(archivo_out, fieldnames=encabezado)
            escritor.writeheader()
            escritor.writerows(ordenados_poblacion)
        
        # 3. Log de éxito
        print(f"\nPaíses ordenados correctamente por población en modo **{modo}** y guardados.")
            
    except FileNotFoundError:
        print("Error: Archivo no encontrado. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al procesar el archivo CSV durante el ordenamiento por población.")

# ------------------------------------------------------------------------
# Lógica para Ordenamiento por Superficie
# ------------------------------------------------------------------------

def obtener_superficie(pais):
    try:
        # Se asegura que la superficie sea un flotante y no sea negativa.
        superficie = float(pais["superficie"])
        if superficie < 0:
            return -1.0
        return superficie
    except (ValueError, KeyError):
        # Si no es un número o la clave falta, devuelve 0.0
        print(f"Advertencia: Superficie inválida ('{pais.get('superficie')}') para '{pais.get('nombre', 'país desconocido')}' ignorada o tratada como 0.")
        return 0.0

def ordenamiento_superficie(opcion):
    
    # 1. Manejo de error de archivo
    if not os.path.exists(RUTA_ARCHIVO):
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Inicializando...")
        inicializar_archivo()
        return

    # Definir el modo para el mensaje de éxito
    modo = "Ascendente (Menor a Mayor)" if opcion == "a" else "Descendente (Mayor a Menor)"

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo_in:
            lector = csv.DictReader(archivo_in)
            paises = list(lector)
            
            if not paises:
                print("El archivo está vacío. No hay países para ordenar.")
                return
            
            # Ordenamiento Ascendente o Descendente (a/d)
            # El manejo de errores de tipo ocurre dentro de la función 'obtener_superficie'
            if opcion == "a":
                ordenados_superficie = sorted(paises, key=obtener_superficie)
            
            elif opcion == "d":
                ordenados_superficie = sorted(paises, key=obtener_superficie, reverse=True)

            else:
                 print("Error de lógica: Opción de ordenamiento inválida recibida.")
                 return
            
        # 2. Escritura del nuevo archivo ordenado
        with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo_out:
            encabezado = ["nombre","poblacion","superficie","continente"]
            escritor = csv.DictWriter(archivo_out, fieldnames=encabezado)
            escritor.writeheader()
            escritor.writerows(ordenados_superficie)
        
        # 3. Log de éxito
        print(f"\nPaíses ordenados correctamente por superficie en modo **{modo}** y guardados.")
            
    except FileNotFoundError:
        print("Error: Archivo no encontrado. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al procesar el archivo CSV durante el ordenamiento por superficie.")

def ordenar_paises():
    
    print("\n" + "=" * 40)
    print("| ORDENAMIENTO DE PAÍSES")
    print("=" * 40)
    
    print("| 1. Por nombre (A-Z)")
    print("| 2. Por población (Asc/Desc)")
    print("| 3. Por superficie (Asc/Desc)")
    print("=" * 40)
    
    try:
        opc_str = input("\nIngrese una opción de ordenamiento (1-3): ").strip()
        
        if not opc_str.isdigit():
             raise ValueError("La opción debe ser un número entero.")
             
        opc = int(opc_str)
        
        # Manejo de casos
        if opc == 1:
            ordenamiento_nombre()
            return
            
        elif opc == 2 or opc == 3:
            
            # Sub-menú para ascendente/descendente
            print("\n" + "-" * 30)
            print("| Seleccione la dirección:")
            print("| Ascendente (a)")
            print("| Descendente (d)")
            print("-" * 30)
            
            opcion_dir = input("\nElige una opción (a/d): ").strip().lower()

            if opcion_dir not in ["a", "d"]:
                print("Error: Opción de dirección inválida. Inténtelo de nuevo.")
                return

            if opc == 2:
                 ordenamiento_poblacion(opcion_dir)
            elif opc == 3:
                 ordenamiento_superficie(opcion_dir)
                 
        else:
             print("❌ Error: Opción inválida. Debe seleccionar un número del 1 al 3.")
            
    except ValueError as e:
        print(f"\nERROR: Entrada inválida. {e}")
        print("Debe ingresar el número de la opción deseada.")
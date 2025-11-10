import csv
import os
from utils import quitar_tildes 
from funciones import inicializar_archivo 

RUTA_ARCHIVO = "ARCHIVO_PAISES\\paises.csv"

#------------------------------------------
# FILTROS
#------------------------------------------

def mostrar_encabezado_tabla():
    """Función auxiliar para imprimir el encabezado de la tabla de resultados."""
    print("-" * 80)
    print(f"{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)' :<17} | {'Continente':<15}")
    print("-" * 80)

def mostrar_fila_pais(pais):
    """Función auxiliar para imprimir una fila de país con manejo de errores de formato."""
    try:
        nombre = pais["nombre"]
        # Intenta la conversión para formato de salida, manejando el posible ValueError
        poblacion = int(pais["poblacion"])
        superficie = float(pais["superficie"])
        continente = pais["continente"]

        print(f"{nombre:<20} | {poblacion:>15} | {superficie:>17.2f} | {continente:<15}")
    except ValueError:
        print(f"{pais.get('nombre', 'País Desconocido'):<20} | {'-- Error de formato --':<60}")


def filtrado_continente():
    print("\n---FILTRAR POR CONTINENTE---")
    continentes_validos = ["america", "europa", "asia", "africa", "oceania", "antartida"]

    # --- 1. Entrada y validación del usuario ---
    continente = input("Ingrese el continente con el que desea filtrar: ").strip().lower()

    if not continente:
        print("Error: Entrada vacía. Inténtelo de nuevo.")
        return

    if continente.isdigit():
        print("Error: No puede ingresar números. Inténtelo de nuevo.")
        return

    if continente not in continentes_validos:
        print(f"Error: El continente ingresado ('{continente}') no es válido. Los válidos son: {', '.join(continentes_validos).capitalize()}.")
        return

    cont_sin_tildes = quitar_tildes(continente)

    # --- 2. Lectura y procesamiento de archivo (con try/except) ---
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            for fila in lector:
                # Se utiliza .get() para evitar KeyError si la columna "continente" falta
                nombre_continente_csv = fila.get("continente", "") 
                if quitar_tildes(nombre_continente_csv.lower()) == cont_sin_tildes:
                    encontrados.append(fila)

            # --- 3. Resultados y Logs ---
            if encontrados:
                print(f"\nSe encontraron **{len(encontrados)}** países en el continente de **{continente.capitalize()}**:")
                mostrar_encabezado_tabla()
                for pais in encontrados:
                    mostrar_fila_pais(pais)
                print("-" * 80)
            else:
                print(f"⚠️ No se encontraron países para el continente **{continente.capitalize()}**.")
                
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe.")
        inicializar_archivo()
    except csv.Error:
        print("Error al procesar el archivo CSV durante el filtrado por continente.")


def filtrado_rango_poblacion():
    print("\n---FILTRAR POR RANGO DE POBLACIÓN---")
    pobl_min, pobl_max = 0, 0
    
    # --- 1. Entrada y validación del usuario (Aislado del bloque de archivo) ---
    try:
        pobl_min_str = input("Ingrese la población mínima (solo números): ").strip()
        if not pobl_min_str:
            print("Error: Población mínima vacía.")
            return

        pobl_max_str = input("Ingrese la población máxima (solo números): ").strip()
        if not pobl_max_str:
            print("Error: Población máxima vacía.")
            return

        # Validación de tipos y conversión a entero, manejando ValueError
        pobl_min = int(pobl_min_str)
        pobl_max = int(pobl_max_str)
        
        if pobl_min < 0 or pobl_max < 0:
            raise ValueError("Las poblaciones no pueden ser negativas.")

        if pobl_min > pobl_max:
            print("Error: La población mínima no puede ser mayor que la población máxima.")
            return

    except ValueError:
        print("Error de tipo: Debe ingresar únicamente números enteros positivos para la población.")
        return

    # --- 2. Lectura y procesamiento de archivo (con try/except) ---
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            for fila in lector:
                try:
                    # Validación y conversión del tipo de dato del archivo
                    poblacion = int(fila.get("poblacion", -1))
                    
                    if pobl_min <= poblacion <= pobl_max:
                        encontrados.append(fila)
                        
                except ValueError:
                    # Ignora filas con datos de población inválidos
                    continue 

            # --- 3. Resultados y Logs ---
            if encontrados:
                print(f"\nSe encontraron **{len(encontrados)}** países con población entre **{pobl_min:,}** y **{pobl_max:,}**:")
                mostrar_encabezado_tabla()
                for pais in encontrados:
                    mostrar_fila_pais(pais)
                print("-" * 80)
            else:
                print(f"No se encontraron países en el rango de población entre {pobl_min:,} y {pobl_max:,}.")
                
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe.")
        inicializar_archivo()
    except csv.Error:
        print("Error al procesar el archivo CSV durante el filtrado por población.")


def filtrado_superficie():
    print("\n---FILTRAR POR RANGO DE SUPERFICIE---")
    sup_min, sup_max = 0.0, 0.0
    
    # --- 1. Entrada y validación del usuario (Aislado del bloque de archivo) ---
    try:
        sup_min_str = input("➡️ Ingrese la superficie mínima (ej: 1000.50): ").strip().replace(',', '.')
        if not sup_min_str:
            print("Error: Superficie mínima vacía.")
            return

        sup_max_str = input("Ingrese la superficie máxima (ej: 50000.0): ").strip().replace(',', '.')
        if not sup_max_str:
            print("Error: Superficie máxima vacía.")
            return

        # Validación de tipos y conversión a float, manejando ValueError
        sup_min = float(sup_min_str)
        sup_max = float(sup_max_str)
        
        if sup_min < 0 or sup_max < 0:
            raise ValueError("Las superficies no pueden ser negativas.")
            
        if sup_min > sup_max:
            print("Error: La superficie mínima no puede ser mayor que la superficie máxima.")
            return
            
    except ValueError:
        print("Error de tipo: Debe ingresar un número válido (entero o decimal) positivo para la superficie.")
        return

    # --- 2. Lectura y procesamiento de archivo (con try/except) ---
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            for fila in lector:
                try:
                    # Validación y conversión del tipo de dato del archivo
                    superficie = float(fila.get("superficie", -1)) 
                    
                    if sup_min <= superficie <= sup_max:
                        encontrados.append(fila)
                        
                except ValueError:
                    # Ignora filas con datos de superficie inválidos
                    continue 

            # --- 3. Resultados y Logs ---
            if encontrados:
                print(f"\nSe encontraron **{len(encontrados)}** países con superficie entre **{sup_min:,.2f}** y **{sup_max:,.2f}** km²:")
                mostrar_encabezado_tabla()
                for pais in encontrados:
                    mostrar_fila_pais(pais)
                print("-" * 80)
            else:
                print(f"⚠️ No se encontraron países en el rango de superficie entre {sup_min:,.2f} y {sup_max:,.2f} km².")
                
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe.")
        inicializar_archivo()
    except csv.Error:
        print("Error al procesar el archivo CSV durante el filtrado por superficie.")


def filtrar_paises():
    
    print("\n" + "=" * 40)
    print("| FILTROS DISPONIBLES")
    print("=" * 40)
    
    print("| 1. Filtrar por continente")
    print("| 2. Filtrar por rango de población")
    print("| 3. Filtrar por rango de superficie")
    print("=" * 40)
    
    try:
        opc_str = input("\nSeleccione una opción de filtro (1-3): ").strip()
        
        if not opc_str.isdigit():
             raise ValueError("La opción debe ser un número entero.")
             
        opc = int(opc_str)

        if opc == 1:
            filtrado_continente()
        elif opc == 2:
            filtrado_rango_poblacion()
        elif opc == 3:
            filtrado_superficie()
        else:
            print("Error: Opción inválida. Debe seleccionar 1, 2, o 3.")
            
    except ValueError as e:
        print(f"\nERROR: Entrada inválida. {e}")
        print("Debe ingresar el número de la opción deseada.")

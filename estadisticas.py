from funciones import RUTA_ARCHIVO, inicializar_archivo
import csv
import os

#------------------------------------------
# ESTADISTICAS
#------------------------------------------

def pais_menor_mayor():
    print("\n---PAÍS CON MAYOR Y MENOR POBLACIÓN---")
    
    # 1. Manejo de error de archivo
    try:
        if not os.path.exists(RUTA_ARCHIVO):
            print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Inicializando...")
            inicializar_archivo()
            return
            
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            # Variables para seguimiento
            nombre_mayor = nombre_menor = None
            may_poblacion = men_poblacion = None
            paises_validos_contados = 0

            for fila in lector:
                # 2. Manejo de errores de formato y clave (KeyError, ValueError)
                try:
                    pobl = int(fila["poblacion"])
                    nombre = fila["nombre"]
                    
                    if pobl < 0:
                        print(f"⚠️ Advertencia: Población negativa ignorada para {nombre}.")
                        continue
                        
                except (ValueError, KeyError):
                    # Ignorar filas con datos de población no numéricos o incompletos
                    # Esto garantiza que el cálculo de Min/Max sea preciso.
                    continue 

                # 3. Lógica de inicialización y comparación
                paises_validos_contados += 1
                
                if nombre_mayor is None: # Usa 'is None' o el contador en lugar de la bandera 'primera'
                    may_poblacion = men_poblacion = pobl
                    nombre_mayor = nombre_menor = nombre
                    
                else:
                    if pobl > may_poblacion:
                        may_poblacion = pobl
                        nombre_mayor = nombre
                        
                    if pobl < men_poblacion:
                        men_poblacion = pobl
                        nombre_menor = nombre

            # 4. Logs de resultados
            if paises_validos_contados == 0:
                print("No hay países con población válida para calcular el mínimo/máximo.")
            else:
                print(f"Resultados basados en {paises_validos_contados} países con datos válidos:")
                print("-" * 50)
                print(f"| País con **mayor** población: {nombre_mayor} | Población: {may_poblacion:,}")
                print(f"| País con **menor** población: {nombre_menor} | Población: {men_poblacion:,}")
                print("-" * 50)

    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al leer el archivo CSV. Verifique el formato.")


def promedio_poblacion():
    print("\n---PROMEDIO DE POBLACIÓN MUNDIAL---")
    total_poblacion = 0
    paises_contables = 0
    
    # 1. Manejo de error de archivo
    try:
        if not os.path.exists(RUTA_ARCHIVO):
            print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Inicializando...")
            inicializar_archivo()
            return

        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            # Suma de la poblacion de cada pais.
            for fila in lector:
                # 2. Manejo de errores de formato y clave (KeyError, ValueError)
                try:
                    poblacion = int(fila["poblacion"])
                    if poblacion >= 0:
                        total_poblacion += poblacion
                        paises_contables += 1
                    else:
                        print(f"Advertencia: Población negativa ignorada para {fila.get('nombre', 'país desconocido')}.")
                except (ValueError, KeyError):
                    print(f"Advertencia: Fila ignorada por valor de población inválido para {fila.get('nombre', 'país desconocido')}.")
                    continue
            
            # 3. Promedio total y manejo de ZeroDivisionError
            if paises_contables == 0:
                print("⚠️ No hay países con población válida para calcular el promedio.")
                return

            prom_poblacion = total_poblacion / paises_contables
            
            # 4. Logs de resultados
            print("-" * 50)
            print(f"| Promedio de población mundial (basado en {paises_contables} países):")
            print(f"| **{round(prom_poblacion):,}** habitantes")
            print("-" * 50)
            
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al leer el archivo CSV. Verifique el formato.")

def promedio_superficie():
    print("\n---PROMEDIO DE SUPERFICIE MUNDIAL---")
    total_superficie = 0.0
    paises_contables = 0
    
    # 1. Manejo de error de archivo
    try:
        if not os.path.exists(RUTA_ARCHIVO):
            print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Inicializando...")
            inicializar_archivo()
            return

        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            # Suma de la superficie de cada pais
            for fila in lector:
                # 2. Manejo de errores de formato y clave (KeyError, ValueError)
                try:
                    superficie = float(fila["superficie"])
                    if superficie >= 0:
                        total_superficie += superficie
                        paises_contables += 1
                    else:
                        print(f"Advertencia: Superficie negativa ignorada para {fila.get('nombre', 'país desconocido')}.")
                except (ValueError, KeyError):
                    print(f"Advertencia: Fila ignorada por valor de superficie inválido para {fila.get('nombre', 'país desconocido')}.")
                    continue
            
            # 3. Promedio total y manejo de ZeroDivisionError
            if paises_contables == 0:
                print("No hay países con superficie válida para calcular el promedio.")
                return
                
            prom_superficie = total_superficie / paises_contables
            
            # 4. Logs de resultados
            print("-" * 50)
            print(f"| Promedio de superficie mundial (basado en {paises_contables} países):")
            print(f"| **{round(prom_superficie, 2):,.2f}** km²")
            print("-" * 50)
            
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al leer el archivo CSV. Verifique el formato.")

def paises_por_continente():
    print("\n---CANTIDAD DE PAÍSES POR CONTINENTE---")
    conteo_continentes = {}
    total_paises = 0

    # 1. Manejo de error de archivo
    try:
        if not os.path.exists(RUTA_ARCHIVO):
            print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Inicializando...")
            inicializar_archivo()
            return
            
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for pais in lector:
                # 2. Manejo de KeyError y estandarización de datos
                try:
                    # Estandariza el nombre del continente para contar correctamente
                    continente = pais["continente"].strip().capitalize()
                    
                    if not continente:
                        print(f"⚠️ Advertencia: País {pais.get('nombre', 'desconocido')} ignorado por continente vacío.")
                        continue
                        
                    # 3. Conteo
                    conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
                    total_paises += 1
                    
                except KeyError:
                    print(f"Advertencia: Fila ignorada por falta de la columna 'continente'.")
                    continue
                
            # 4. Logs de resultados
            if total_paises == 0:
                 print("⚠️ No se encontraron países válidos para el conteo.")
                 return
                 
            print(f"Conteo completado (Total de países procesados: {total_paises}):")
            print("-" * 40)
            for continente, cantidad in conteo_continentes.items():
                print(f"| Continente **{continente}**: {cantidad} países")
            print("-" * 40)
            
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe. Creando uno nuevo...")
        inicializar_archivo()
    except csv.Error:
        print("Error al leer el archivo CSV. Verifique el formato.")

def mostrar_estadisticas():
    
    print("\n" + "=" * 40)
    print("| ESTADÍSTICAS MUNDIALES")
    print("=" * 40)
    
    print("| 1. País con menor y mayor población")
    print("| 2. Promedio de población")
    print("| 3. Promedio de superficie")
    print("| 4. Cantidad de países por continente")
    print("=" * 40)
    
    try:
        opc_str = input("\nIngrese una opción de estadística (1-4): ").strip()
        
        if not opc_str.isdigit():
             raise ValueError("La opción debe ser un número entero.")
             
        opc = int(opc_str)

        if opc == 1:
            pais_menor_mayor()
        elif opc == 2:
            promedio_poblacion()
        elif opc == 3:
            promedio_superficie()
        elif opc == 4:
            paises_por_continente()
        else:
            print("❌ Error: Opción inválida. Debe seleccionar un número del 1 al 4.")
            
    except ValueError as e:
        print(f"\nERROR: Entrada inválida. {e}")
        print("Debe ingresar el número de la opción deseada.")
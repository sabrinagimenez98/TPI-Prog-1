import csv, os
from utils import quitar_tildes

RUTA_ARCHIVO = "ARCHIVO_PAISES/paises.csv"

#--------------------------
#FUNCIONES PROGRAMA
#------------------------- 

#Funcion para crear archivo si no existe
def inicializar_archivo():
    os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
    if not os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            #Crea una lista de diccionarios y toma la primer linea/fila como encabezados como (key), y los demas como (value)
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            #escribe los encabezados en el archivo
            escritor.writeheader()

#--------------------------
#FUNCIONES MENU
#--------------------------

def mostrar_paises():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            #lee el contenido del archivo como lista de diccionarios
            contenido = list(csv.DictReader(archivo))
            if not contenido:
                print("No hay países registrados.")
                return
            # Encabezado con ancho fijo
            print("-" * 70)
            print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
            print("-" * 70)
            #Paises
            for fila in contenido:
                try:
                    nombre =fila['nombre']
                    poblacion = int(fila['poblacion'])
                    superficie = float(fila['superficie'])
                    continente = quitar_tildes(fila['continente'])
                    print(f"{nombre:<20} | {poblacion:>12} | {superficie:>14} | {continente:>15} |")
                except ValueError:
                     #elimina paises con errores de formato
                    print(f"- País {fila.get('nombre')}' eliminado por error de formato.")
    except FileNotFoundError:
        inicializar_archivo()

def buscar_pais():
    pais = input("Ingrese el nombre del país: ").strip()
    if not pais or pais.isdigit():
        print("Entrada inválida.")
        return
    #Quito las tildes al pais ingresado para la comparacion.
    pais = quitar_tildes(pais.lower())
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector=csv.DictReader(archivo)
            for fila in lector:
                 #Comparacion
                if quitar_tildes(fila["nombre"].lower()) == pais:
                    print(f"{fila['nombre']} | Población: {fila['poblacion']} | Superficie: {fila['superficie']} | Continente: {fila['continente']}")
                    return
        print("País no encontrado.")
    except FileNotFoundError:
        inicializar_archivo()

def agregar_pais():
    nombre = input("Nombre del país: ").strip().title()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie: ").strip()
    continente = input("Continente: ").strip().title()
    if not nombre or not poblacion.isdigit() or not superficie.replace('.', '', 1).isdigit():
        print("Datos inválidos.")
        return
    nuevo = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    with open(RUTA_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=nuevo.keys())
        escritor.writerow(nuevo)
    print("País agregado.")

def eliminar_pais():
    nombre = input("Ingrese el país a eliminar: ").strip().lower()
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            paises = list(csv.DictReader(archivo))
        nuevos = [p for p in paises if quitar_tildes(p["nombre"].lower()) != quitar_tildes(nombre)]
        if len(nuevos) < len(paises):
            with open(RUTA_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
                escritor.writeheader()
                escritor.writerows(nuevos)
            print("País eliminado.")
        else:
            print("País no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

from funciones import RUTA_ARCHIVO
import csv
from utils import quitar_tildes

def filtrar_paises():
    print("1. Por continente\n2. Por población\n3. Por superficie")
    opc = input("Seleccione filtro: ").strip()
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        paises = list(csv.DictReader(archivo))
    if opc == "1":
        cont = input("Ingrese continente: ").strip().lower()
        filtrados = [p for p in paises if quitar_tildes(p["continente"].lower()) == cont]
    elif opc == "2":
        min_p = int(input("Población mínima: "))
        max_p = int(input("Población máxima: "))
        filtrados = [p for p in paises if min_p <= int(p["poblacion"]) <= max_p]
    elif opc == "3":
        min_s = float(input("Superficie mínima: "))
        max_s = float(input("Superficie máxima: "))
        filtrados = [p for p in paises if min_s <= float(p["superficie"]) <= max_s]
    else:
        print("Opción inválida.")
        return
    for f in filtrados:
        print(f"{f['nombre']} | {f['poblacion']} | {f['superficie']} | {f['continente']}")

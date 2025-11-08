from funciones import RUTA_ARCHIVO
import csv
from collections import Counter

def mostrar_estadisticas():
    with open(RUTA_ARCHIVO, "r", encoding="latin-1") as archivo:
        paises = list(csv.DictReader(archivo))
    if not paises:
        print("⚠️ No hay datos.")
        return
    poblaciones = [int(p["poblacion"]) for p in paises]
    superficies = [float(p["superficie"]) for p in paises]
    continentes = [p["continente"] for p in paises]

    mayor = max(paises, key=lambda x: int(x["poblacion"]))
    menor = min(paises, key=lambda x: int(x["poblacion"]))
    print(f"🌍 Mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"🌎 Menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"📊 Promedio población: {sum(poblaciones)//len(poblaciones)}")
    print(f"📐 Promedio superficie: {round(sum(superficies)/len(superficies), 2)}")
    print("📌 Países por continente:")
    for cont, cant in Counter(continentes).items():
        print(f" - {cont}: {cant}")

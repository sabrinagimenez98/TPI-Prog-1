from funciones import RUTA_ARCHIVO
import csv

def ordenar_paises():
    print("1. Por nombre\n2. Por población\n3. Por superficie")
    opc = input("Seleccione orden: ").strip()
    orden = input("Ascendente (a) o descendente (d): ").strip().lower()
    reverse = orden == "d"
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        paises = list(csv.DictReader(archivo))
    if opc == "1":
        paises.sort(key=lambda x: x["nombre"], reverse=reverse)
    elif opc == "2":
        paises.sort(key=lambda x: int(x["poblacion"]), reverse=reverse)
    elif opc == "3":
        paises.sort(key=lambda x: float(x["superficie"]), reverse=reverse)
    else:
        print("Opción inválida.")
        return
    for p in paises:
        print(f"{p['nombre']} | {p['poblacion']} | {p['superficie']} | {p['continente']}")


from funciones import mostrar_paises, buscar_pais, agregar_pais,eliminar_pais
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas
from filtros import filtrar_paises

def menu():
    while True:
        print("=" * 30)
        print("\nMENÚ PRINCIPAL")
        print("1. Mostrar países")
        print("2. Buscar país")
        print("3. Filtrar países")
        print("4. Ordenar países")
        print("5. Estadísticas")
        print("6. Agregar país")
        print("7. Eliminar país")
        print("8. Salir")
        print("=" * 30)

        try:
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1: mostrar_paises()
                case 2: buscar_pais()
                case 3: filtrar_paises()
                case 4: ordenar_paises()
                case 5: mostrar_estadisticas()
                case 6: agregar_pais()
                case 7: eliminar_pais()
                case 8:
                    print("¡Hasta luego!")
                    break
                case _: print("Opción inválida.")
        except ValueError:
            print("Error: debe ingresar un número.")

menu()

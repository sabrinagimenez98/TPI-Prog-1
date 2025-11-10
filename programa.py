from funciones import mostrar_paises, buscar_pais, agregar_pais, eliminar_pais
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas
from filtros import filtrar_paises

#--------------------------
# RUTA ARCHIVO
#--------------------------

RUTA_ARCHIVO = "ARCHIVO_PAISES\\paises.csv"

def menu():
    
    while True:
        # Imprime el menú principal
        print("\n" + "=" * 40)
        print("MENÚ PRINCIPAL")
        print("=" * 40)
        
        print("| 1. Mostrar todos los países")
        print("| 2. Buscar país (por nombre)")
        print("| 3. Filtrar países (por continente/rango)")
        print("| 4. Ordenar países (por nombre/datos)")
        print("| 5. Mostrar estadísticas (promedios/conteo)")
        print("| 6. Agregar nuevo país")
        print("| 7. Eliminar país")
        print("| 8. **SALIR**")
        print("=" * 40)
            
        try:
            opcion = input("\nSeleccione una opción (1-8): ").strip()
            
            # 1. Validación de entrada (evita que el programa falle con letras)
            if not opcion.isdigit():
                raise ValueError("La opción debe ser un número.")
                
            opcion = int(opcion)

            # 2. Manejo de las opciones
            match opcion:
                case 1: 
                    mostrar_paises()
                case 2: 
                    buscar_pais()
                case 3: 
                    filtrar_paises()
                case 4: 
                    ordenar_paises()
                case 5: 
                    mostrar_estadisticas()
                case 6: 
                    agregar_pais()
                case 7: 
                    eliminar_pais()
                case 8:
                    print("¡Hasta luego!")
                    break
                case _: print("Opción inválida.")

        except ValueError as e:
            # Captura si el usuario ingresa texto en lugar de números para la opción del menú
            print("\n" + "=" * 40)
            print(f"ERROR: Entrada inválida. {e}")
            print("Por favor, ingrese el número de la opción deseada (1-8).")
            print("=" * 40)


#--------------------------
# PRINCIPAL
#--------------------------

if __name__ == "__main__":
    menu()
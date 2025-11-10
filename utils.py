import unicodedata

#------------------------------------------
# UTILIDADES GENERALES
#------------------------------------------

def quitar_tildes(texto):
    """
    Función que elimina las tildes (acentos) y otros diacríticos de una cadena de texto.
    Esto es crucial para realizar comparaciones y búsquedas de nombres de países/continentes
    de manera insensible a los acentos (ej: "América" == "America").
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto) 
        if unicodedata.category(c) != 'Mn')

def validar_entero(mensaje):
    """
    Solicita una entrada al usuario y la valida repetidamente hasta que se 
    ingresa un número entero positivo (cifra digital).
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and int(entrada) >= 0:
            return int(entrada)
        print("❌ Entrada incorrecta. Debes ingresar un número entero positivo (cifra digital).")
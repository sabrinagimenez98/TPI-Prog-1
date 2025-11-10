# 💻Trabajo Práctico Integrador –- Programación 1💻

## Gestión de Países con archivos CSV

### 📕 Integrantes: Sabrina gimenez e Ismael saleme

### Enlace video demostrativo: 

### Marco teorico

### Listas
Las listas son  estructuras ordenadas y mutables ya que permiten modificar los valores de sus elementos, eliminar o añadir elementos.
En ellas se pueden almacenar tantos elementos como se desee, incluso pueden existir listas vacías (sin elementos). Para definirlas se utilizan corchetes y se separan los elementos mediante. Ejemplo: `nombre_lista = [valor1, valor2, ...]`.
En este trabajo las utilizamos para representar colecciones de países, poblaciones, superficies, etc.
### Diccionarios
Un diccionario es una colección mutable y desordenada de elementos, donde cada uno está compuesto por un par único de clave-valor. Ejemplo: mi_diccionario = {"nombre": "Alice", "edad": 25, "profesión": "Ingeniera"}
En este trabajo fue la Estructura clave–valor nos permite acceder rápidamente a atributos de cada país y para representar registros con nombre, población, superficie y continente.
### Funciones
Una función es un bloque de código que realiza una tarea específica. Al usar funciones es posible dividir un problema en partes pequeñas y manejables. Se compone de:
- Entrada (argumentos): datos que recibe la función.
- Proceso: instrucciones que realiza.
- Salida (retorno): resultado que devuelve.
Son muy útiles ya que permiten reutilizar una porción de código tantas veces como sea necesario.
La palabra reservada para definir una función es `def`. Para crearla debemos indicar un nombre para la función y establecer sus argumentos.
La estructura que se usa para definir funciones es la siguiente:
def nombre_funcion(nombre_argumento):
    código a ejecutar
    return valor_de_retorno
Ejemplo:
def saludar():
    return "¡Hola! ¿Cómo estás?"
saludo = saludar()
print(saludo)
Nos permite dividir el programa en bloques reutilizables, cada uno con una tarea específica. Facilitan la organización, el mantenimiento y la legibilidad del código.
### Condicionales
Los condicionales son estructuras de control que permiten ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa. La instrucción más básica para realizar una evaluación condicional es la sentencia `if`, que evalúa una expresión booleana (es decir, una expresión que puede ser verdadera o falsa) y ejecuta un bloque de código sólo si la condición se cumple. Además, se pueden usar otras estructuras como `elif` (abreviatura de "else if") y `else` para manejar diferentes casos o situaciones, ofreciendo una mayor flexibilidad en la lógica del programa. Las condicionales son fundamentales para la toma de decisiones en los programas, permitiendo que el flujo de ejecución se ajuste dinámicamente según las circunstancias.
Ejemplo:
if puntuación >= 90:
   print("Excelente")
elif puntuación >= 70:
   print("Bueno")
else:
   print("Necesitas mejorar")
Nos permiten tomar decisiones en el programa según ciertas condiciones. Se usan para validar entradas, aplicar filtros y mostrar mensajes adecuados.
### Ordenamientos
Los métodos de ordenamiento son algoritmos que realizan la operación de arreglar los registros de una tabla en algún orden secuencial de acuerdo a un criterio de ordenamiento. El ordenamiento se efectúa con base en el valor de algún campo en un grupo de datos. El ordenamiento puede estar dado de forma iterativa o recursiva según la naturaleza y forma de ejecución del mismo.
Ejemplos de métodos de ordenamiento: BubbleSort, SelectionSort, InsertionSort, etc.
Se aplican para organizar los países según criterios como nombre, población o superficie. Se utiliza sorted() con funciones key personalizadas.
### Estadísticas básicas
Son funciones que  calculan el promedio o el valor típico de una población o muestra.
Los aplicamos para obtener indicadores relevantes del dataset.
### Archivos CSV
Los archivos CSV (Comma Separated Values) son similares a planillas: cada línea
representa una fila, y los valores están separados por comas.
Ejemplo de archivo productos.csv
Formato de texto plano que permite almacenar datos estructurados. Utilizamos el módulo csv para leer y procesar los registros de países.

### Flujo de operaciones principales

Mapa conceptual en PDF

### 📌 Descripción del programa
Este proyecto es una aplicación de consola escrita en Python que administra un registro de países almacenado en un archivo CSV.  
Permite realizar tareas variadas de consulta, búsqueda, filtrado, ordenamiento y estadísticas sobre cada país, además de agregar y eliminar registros.

Cada país del dataset posee:
- **Nombre**
- **Población**
- **Superficie (km²)**
- **Continente**

El sistema trabaja leyendo y escribiendo datos directamente en paises.csv utilizando diccionarios, listas y manejo de archivos con la librería csv.

---

### ✅ Funcionalidades principales
✔ Mostrar todos los países registrados en formato tabla  
✔ Buscar país por nombre
✔ Filtrar por:
- Continente
- Rango de población
- Rango de superficie

✔ Ordenar por:
- Nombre
- Población
- Superficie  
(en forma ascendente o descendente)

✔ Estadísticas:
- País con mayor población
- País con menor población
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente

✔ Agregar un país al archivo  
✔ Eliminar un país por nombre  
✔ Verificación y validación de entradas del usuario  
✔ Manejo de errores y registros con formato incorrecto  

---

### 📜 Instrucciones de uso

1. **Requisitos**
   - Python **3.10+** (necesario porque se usa match/case)
   - Librerías estándar de Python (no requiere instalación extra)

2. **Ejecución**
   - Abrir la carpeta del proyecto
   - Ejecutar el archivo principal:
     
     python PRACTICA_INTEGRADO.py
   
   - Se mostrará un menú numérico con opciones.

3. **Archivo CSV**
   - No es necesario crearlo manualmente.
   - Si no existe paises.csv, el programa lo inicializa automáticamente.
   - Las modificaciones (agregar, eliminar, ordenar) quedan guardadas en el archivo.

---

### 🧪 Ejemplos de uso

#### ✅ Opcion 1 – Mostrar países
**Entrada (usuario): 1**

<img width="843" height="437" alt="imagen" src="https://github.com/user-attachments/assets/0990559a-6f13-4a97-92dc-9ce45a50510c" />

#### ✅ Opcion 2 – Buscar pais (por nombre)
**Entrada (usuario): 2**

<img width="886" height="91" alt="imagen" src="https://github.com/user-attachments/assets/06ec63cd-6379-4086-90bd-7be7d299add6" />

#### ✅ Opcion 3 – Filtar paises
**Entrada (usuario): 3**

<img width="873" height="118" alt="imagen" src="https://github.com/user-attachments/assets/4a47f6a2-bdec-4d7c-9d9c-6eb957fb7ad2" />

- **Filtrado por continente**

<img width="775" height="410" alt="imagen" src="https://github.com/user-attachments/assets/00c8856f-c785-4c7f-85aa-18212168ead8" />

- **Filtrado por poblacion**

<img width="813" height="432" alt="imagen" src="https://github.com/user-attachments/assets/b754f9b4-823f-4372-86a2-b9bf7ca432e1" />

- **Filtrado por superficie**

<img width="848" height="428" alt="imagen" src="https://github.com/user-attachments/assets/a65f8d97-ec84-42a9-b0a1-9445cc474fdf" />

#### ✅ Opcion 4 – Ordenar paises

<img width="843" height="261" alt="imagen" src="https://github.com/user-attachments/assets/0e60e66e-5631-4404-8cbd-002caf41d7d4" />

- **Ordenamiento por nombre (alfabeticamente)**

  <img width="829" height="432" alt="imagen" src="https://github.com/user-attachments/assets/53fd1615-13d8-43d2-a494-b9b185e89ad2" />

- **Ordenamiento por poblacion (Ascendente o Descendente)**

<img width="829" height="141" alt="imagen" src="https://github.com/user-attachments/assets/e4a16bce-6409-4782-955b-a56ba68c7e41" />

- ***Ascendente***

  <img width="821" height="411" alt="imagen" src="https://github.com/user-attachments/assets/15a5c8ba-7871-4def-9400-e70a193441a0" />

- ***Descendente***

  <img width="814" height="430" alt="imagen" src="https://github.com/user-attachments/assets/b909c0f4-bf95-4107-a26c-98a85be99e9c" />

- **Ordenamiento por superficie (Ascendente o Descendente)**
- ***Se comporta de igual manera que la opcion anterior***

#### ✅ Opcion 5 – Mostrar estadisticas

<img width="885" height="151" alt="imagen" src="https://github.com/user-attachments/assets/4a4f84d2-df13-415d-9c47-62a95934a04e" />

- **Menor y mayor**

- <img width="662" height="140" alt="imagen" src="https://github.com/user-attachments/assets/05da77f2-5bdf-4f56-9e5f-0c8f59843dc5"> 

- **Promedio poblacion**

  <img width="862" height="78" alt="imagen" src="https://github.com/user-attachments/assets/aaeebb73-3ab8-4bb1-8234-b37e70ea4bf2" />

- **Promedio superficie**

  <img width="862" height="74" alt="imagen" src="https://github.com/user-attachments/assets/5243d32e-027c-4222-9872-973114a24f25" />

- **Cantidad de paises por continente**

  <img width="862" height="114" alt="imagen" src="https://github.com/user-attachments/assets/f95f888d-63ea-4f45-855d-0412a1c0d24f" />


#### ✅ Opcion 6 – Agregar pais

<img width="841" height="108" alt="imagen" src="https://github.com/user-attachments/assets/d37f4dfc-ebd8-438d-95f6-2c6736772fbe" />

<img width="885" height="43" alt="imagen" src="https://github.com/user-attachments/assets/03f8ca53-1d90-4621-bc25-3ea2a3ccde4b" />

#### ✅ Opcion 7 – Eliminar pais

<img width="885" height="92" alt="imagen" src="https://github.com/user-attachments/assets/503e1757-efc6-4417-87ad-8dcf16cc659b" />

<img width="885" height="22" alt="imagen" src="https://github.com/user-attachments/assets/9175b92c-9ef0-44da-8390-c27ed6416e63" />

#### ✅ Opcion 8 – Salir del programa

<img width="885" height="41" alt="imagen" src="https://github.com/user-attachments/assets/e67409f6-3ef0-4ea3-8c5e-f51d28b88d8e" />

### Conclusion resumida (conclusion completa en PDF)

En resumen, este trabajo integrador fue una experiencia que nos permitió aplicar la mayoría de los contenidos de Programación 1 en un contexto real, desarrollar un sistema completo y fortalecer tanto nuestras habilidades técnicas como nuestras habilidades colaborativas.

### Referencias

Adjuntas en el PDF

### 👥 Participación de los integrantes
#### Trabajo realizado por:

- **Sabrina gimenez** – Desarrollo del menú principal, manejo de archivos y carga/ eliminación de países y documentacion
- **Ismael saleme** – Implementación de filtros, ordenamientos y estadísticas, Testeo, validaciones y documentación.
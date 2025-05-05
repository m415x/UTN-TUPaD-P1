# Ejercicio 1: Bucle for para números pares
# Objetivo: Imprimir números pares usando un bucle for.
# Instrucciones:
# 1. Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).
# 2. Usa un condicional o el paso del rango para lograrlo.
# Preguntas de reflexión:
# • ¿Cómo modificarías el código para imprimir solo impares?
# * Respuesta: Cambiando el paso del rango a 1 o usando un condicional para filtrar los números impares.
# • ¿Qué pasa si el rango fuera de 2 a 20 con paso 3?
# * Respuesta: Imprimiría los números 2, 5, 8, 11, 14, 17.

for i in range(2, 21, 2):
    print(i)

# print("\n".join(f"{i}" for i in range(2, 21, 2)))

# Ejercicio 2: Bucle while con suma acumulativa
# Objetivo: Usar un bucle while para controlar una condición de salida.
# Instrucciones:
# 1. Pide al usuario que ingrese números hasta que la suma supere 100.
# 2. Imprime la suma total al final.
# Preguntas de reflexión:
# • ¿Qué ocurre si el primer número ingresado es mayor que 100?
# * Respuesta: El bucle finalizaría inmediatamente y la suma total sería el número ingresado.
# • ¿Cómo evitarías errores si el usuario ingresa texto?
# * Respuesta: Usando un condicional para verificar si el input es un número antes de sumarlo. Si no es numero, salta a la siguiente iteración.

numero = 0
suma = 0
while suma <= 100:
    numero = int(input("Ingrese un número: "))
    suma += numero
print(f"La suma total es: {suma}")

# Ejercicio 3: Filtrar palabras por letra inicial
# Objetivo: Iterar sobre una lista y aplicar filtros.
# Instrucciones:
# 1. Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), imprime
# solo las que empiezan con "a".
# Preguntas de reflexión:
# • ¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también se cuente)?
# * Respuesta: Transformando las cadenas a minúsculas antes de compararlas.
# • ¿Qué método de strings es útil para esto?
# * Respuesta: El método lower() convierte una cadena a minúsculas.

palabras = ["apple", "banana", "avocado", "manzana", "arándano"]
for palabra in palabras:
    if palabra.lower().startswith("a"):
        print(palabra)

# Ejercicio 4: Tabla de multiplicar del 7
# Objetivo: Usar un bucle para generar patrones.
# Instrucciones:
# 1. Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).
# Preguntas de reflexión:
# • ¿Cómo adaptarías el código para que el usuario elija la tabla?
# * Respuesta: Usando input() para que el usuario ingrese el número de la tabla que desea.
# • ¿Qué estructura usarías para almacenar los resultados?
# * Respuesta: Podría usar una lista para almacenar los resultados de la tabla de multiplicar.

for i in range(1, 11):
    tabla = 7
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")

# Ejercicio 5: Contador de vocales
# Objetivo: Contar caracteres específicos en un string.
# Instrucciones:
# 1. Pide al usuario una cadena de texto.
# 2. Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.
# Preguntas de reflexión:
# • ¿Cómo manejarías las vocales acentuadas (á, é)?
# * Respuesta: Agregando las vocales acentuadas a la cadena de vocales.
# • ¿Qué estructura de datos te ayudaría a optimizar el código?
# * Respuesta: Una lista o un conjunto (set) para almacenar las vocales y verificar su presencia.

cadena = input("Ingrese una cadena de texto: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1
print(f"La cadena contiene {contador} vocales.")

# Ejercicio 6: Números repetidos en una lista
# Objetivo: Filtrar elementos duplicados manteniendo el orden.
# Instrucciones:
# 1. Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los números que
# aparecen más de una vez (en este caso: [3, 1]).
# Preguntas de reflexión:
# • ¿Por qué es importante mantener el orden de aparición?
# * Respuesta: Para preservar la secuencia original y facilitar la comprensión del resultado.
# • ¿Cómo resolverías esto sin usar estructuras adicionales?
# * Respuesta: Usando un bucle anidado para comparar cada elemento con los demás y agregarlo a la lista de repetidos si se encuentra más de una vez.

lista_original = [3, 1, 3, 5, 1]
repetidos = []
for i in range(len(lista_original)):
    if lista_original[i] in repetidos:
        continue
    for j in range(i + 1, len(lista_original)):
        if lista_original[i] == lista_original[j]:
            repetidos.append(lista_original[i])
            break
print(f"Números repetidos: {repetidos}")

# Ejercicio 7: FizzBuzz
# Objetivo: Implementar lógica condicional en bucles.
# Instrucciones:
# 1. Imprime números del 1 al 100, pero:
# o Para múltiplos de 3 → "Fizz".
# o Para múltiplos de 5 → "Buzz".
# o Para múltiplos de ambos → "FizzBuzz".
# Preguntas de reflexión:
# • ¿Por qué el orden de los condicionales es crucial aquí?
# * Respuesta: Porque si primero verificamos si es múltiplo de 3 y luego de 5, nunca se imprimirá "FizzBuzz".
# • ¿Cómo extenderías el juego a otros números (ej: 7 → "Bazz")?
# * Respuesta: Agregando más condiciones al bloque if-elif-else para verificar otros múltiplos.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Ejercicio 8: Frecuencia de palabras
# Objetivo: Usar diccionarios para contar elementos.
# Instrucciones:
# 1. Dada una cadena (ej: "hola hola mundo"), devuelve un diccionario con la
# frecuencia de cada palabra (ej: {"hola": 2, "mundo": 1}).
# Preguntas de reflexión:
# • ¿Cómo ignorarías signos de puntuación (ej: "hola," vs "hola")?
# * Respuesta: Usando el método .strip() para eliminar signos de puntuación al inicio y al final de cada palabra.
# • ¿Qué método de strings ayuda a separar palabras?
# * Respuesta: El método .split() separa una cadena en una lista de palabras.

cadena = "hola hola mundo"
palabras = cadena.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print(f"Frecuencia de palabras: {frecuencia}")

# Ejercicio 9: Filtrar consonantes
# Objetivo: Manipular strings con condiciones.
# Instrucciones:
# 1. Dada una cadena, crea una nueva cadena que solo contenga
# sus consonantes (ej: "Hola" → "Hl").
# Preguntas de reflexión:
# • ¿Cómo manejarías las mayúsculas/minúsculas?
# * Respuesta: Usando el método .lower() para convertir todo a minúsculas antes de comparar.
# • ¿Qué estructura usarías para definir las consonantes?
# * Respuesta: Una cadena de texto que contenga todas las consonantes del alfabeto.

cadena = "Hola mundo!"
vocales = "aeiou"
nueva_cadena = ""
for letra in cadena:
    if letra.lower() not in vocales:
        nueva_cadena += letra
print(f"Cadena original: {cadena}")
print(f"Cadena con consonantes: {nueva_cadena}")

# Ejercicio 10: Números primos
# Objetivo: Implementar un algoritmo con bucles anidados.
# Instrucciones:
# 1. Pide al usuario un número entero positivo.
# 2. Imprime todos los números primos menores o iguales a ese número.
# Preguntas de reflexión:
# • ¿Cómo optimizarías la verificación de primos?
# * Respuesta: Verificando divisibilidad solo hasta la raíz cuadrada del número.
# • ¿Qué ventaja tiene usar range(2, int(n**0.5) + 1)?
# * Respuesta: Reduce el número de iteraciones necesarias para verificar si un número es primo,
# * mejorando la eficiencia del algoritmo.
# Bonus:
# • Diagrama de flujo: Elige un ejercicio y dibuja su diagrama de flujo.
# • Reto extra: Modifica un ejercicio para usar break o continue.

numero = int(input("Ingrese un número entero positivo: "))
primos = []
for i in range(2, numero + 1):
    es_primo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(i)
print(f"Números primos menores o iguales a {numero}: {primos}")

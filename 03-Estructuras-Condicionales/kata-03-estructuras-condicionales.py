# Ejercicio 1: Validación de contraseña
# Objetivo: Analizar un programa existente que verifica una contraseña.
# Instrucciones:
# 1. Lee el siguiente código y explica qué hace:
# contrasena_correcta = "programacion1"
# contrasena_usuario = input("Introduce la contraseña: ")
# if contrasena_usuario == contrasena_correcta:
#     print("Contraseña correcta. Bienvenido.")
# else:
#     print("Contraseña incorrecta. Intenta de nuevo.")
# Preguntas de reflexión:
# • ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas?
# * Respuesta: Si el usuario ingresa la contraseña con mayúsculas, el programa no la
# * reconocerá como correcta, ya que la comparación es sensible a mayúsculas y minúsculas.
# • ¿Cómo mejorarías el programa para dar más intentos?
# * Respuesta: Podría usar un bucle que permita al usuario ingresar la contraseña varias veces
# * antes de finalizar el programa. Por ejemplo, se podría usar un bucle while que permita al usuario
# * ingresar la contraseña hasta un número máximo de intentos. Si el usuario ingresa la contraseña correcta,
# * el programa termina, de lo contrario, se le informa que ha agotado sus intentos.

# Definimos la contraseña correcta
contrasena_correcta = "programacion1"
# Pedimos al usuario que ingrese la contraseña
contrasena_usuario = input("Introduce la contraseña: ")
# Comparamos la contraseña ingresada por el usuario con la correcta
if contrasena_usuario == contrasena_correcta:
    # Si son iguales, imprimimos un mensaje de bienvenida y el programa termina
    print("Contraseña correcta. Bienvenido.")
else:
    # Si no son iguales, imprimimos un mensaje de error y el programa termina
    print("Contraseña incorrecta. Intenta de nuevo.")

# Ejercicio 2: Identificador de vocales
# Objetivo: Clasificar caracteres usando condicionales.
# Instrucciones:
# 1. Solicita una letra al usuario.
# 2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra
# ingresada es una vocal".
# 3. En otro caso, imprime: "La letra ingresada no es una vocal".
# Preguntas de reflexión:
# • ¿Cómo manejarías vocales acentuadas (á, é)?
# * Respuesta: Para manejar vocales acentuadas, se podría ampliar la lista de vocales
# * a incluir las vocales acentuadas. Por ejemplo, se podría usar la siguiente lista:
# * ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"].
# • ¿Qué estructura usarías para simplificar las comparaciones?
# * Respuesta: Se podría usar una lista o un conjunto para almacenar las vocales y luego
# * verificar si la letra ingresada está en esa lista o conjunto. Esto haría el código más limpio y fácil de leer.

letra = input("Introduce una letra: ").lower()
if letra in ["a", "e", "i", "o", "u"]:
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada no es una vocal.")

# Ejercicio 3: Clasificador de números
# Objetivo: Determinar el signo de un número.
# Instrucciones:
# 1. Pide un número al usuario.
# 2. Si es positivo, imprime: "El número es positivo".
# 3. Si es negativo, imprime: "El número es negativo".
# 4. Si es cero, imprime: "El número es cero".
# Preguntas de reflexión:
# • ¿Qué ocurre si el usuario ingresa un texto?
# * Respuesta: Si el usuario ingresa un texto, el programa generará un error de tipo (TypeError) al intentar comparar
# * el texto con un número.
# • ¿Cómo adaptarías el código para números decimales?
# * Respuesta: Para adaptar el código a números decimales, se podría usar la función float() para convertir la entrada
# * del usuario a un número decimal. Esto permitiría que el programa funcione correctamente con números decimales.

numero = int(input("Introduce un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejercicio 4: Comparador de números
# Objetivo: Comparar dos números con condicionales.
# Instrucciones:
# 1. Solicita dos números al usuario.
# 2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
# 3. Si el primero es menor, imprime: "El primer número ingresado es menor".
# 4. Si son iguales, imprime: "Los números ingresados son iguales".
# Preguntas de reflexión:
# • ¿Cómo modificarías el programa para comparar más de dos números?
# * Respuesta: Para comparar más de dos números, se podría usar una lista para almacenar los números ingresados y luego
# * usar la función max() para encontrar el número mayor y la función min() para encontrar el número menor. Luego, se podría
# * comparar cada número con el mayor y el menor para determinar si son iguales o no.
# • ¿Qué pasa si se ingresan valores no numéricos?
# * Respuesta: Si se ingresan valores no numéricos, el programa generará un error de tipo (TypeError) al intentar comparar
# * los valores no numéricos con números.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
if numero1 > numero2:
    print("El primer número ingresado es mayor.")
elif numero1 < numero2:
    print("El primer número ingresado es menor.")
else:
    print("Los números ingresados son iguales.")

# Ejercicio 5: Clima según temperatura
# Objetivo: Clasificar temperaturas en rangos.
# Instrucciones:
# 1. Pide la temperatura actual en °C.
# 2. Si es ≤ 10°C, imprime: "Hace frío".
# 3. Si está entre 10°C y 25°C, imprime: "Está templado".
# 4. Si es > 25°C, imprime: "Hace calor".
# Preguntas de reflexión:
# • ¿Cómo adaptarías el programa para usar °F?
# * Respuesta: Para adaptar el programa para usar °F, se podría usar la fórmula de conversión de °F a °C:
# * °C = (°F - 32) * 5/9. Luego, se podría pedir al usuario que ingrese la temperatura en °F y convertirla a °C antes de hacer las comparaciones.
# • ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
# * Respuesta: Para añadir más rangos, se podrían definir nuevos límites de temperatura y agregar más condiciones if-elif para cada rango adicional.
# * Por ejemplo, se podría agregar una condición para temperaturas < 0°C que imprima "Hace mucho frío". O >35°C que imprima "Hace mucho calor".

temperatura = int(input("Introduce la temperatura actual en °C: "))
if temperatura <= 10:
    print("Hace frío.")
elif 10 < temperatura <= 25:
    print("Está templado.")
else:
    print("Hace calor.")

# Ejercicio 6: Detector de años bisiestos
# Objetivo: Aplicar condiciones compuestas.
# Instrucciones:
# 1. Pide un año al usuario.
# 2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se
# ingresó un año bisiesto".
# 3. En otro caso, imprime: "Se ingresó un año no bisiesto".
# Preguntas de reflexión:
# • ¿Por qué el año 1900 no es bisiesto?
# * Respuesta: El año 1900 no es bisiesto porque, aunque es divisible por 4, también es divisible por 100 y no es divisible por 400.
# • ¿Cómo validarías que el año sea positivo?
# * Respuesta: Para validar que el año sea positivo, se podría usar una condición if para verificar si el año es mayor que 0 antes de hacer las comparaciones.
# * Si el año no es positivo, se podría imprimir un mensaje de error y pedir al usuario que ingrese un año válido.

year = int(input("Introduce un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Se ingresó un año bisiesto.")
else:
    print("Se ingresó un año no bisiesto.")

# Ejercicio 7: Ajustador de frases
# Objetivo: Manipular strings con condicionales.
# Instrucciones:
# 1. Pide una frase o palabra al usuario.
# 2. Si no termina en punto, añádelo al final.
# 3. Imprime el resultado.
# Preguntas de reflexión:
# • ¿Cómo manejarías frases que terminan con espacios?
# * Respuesta: Para manejar frases que terminan con espacios, se podría usar el método .strip() para eliminar los espacios en blanco
# * al principio y al final de la cadena antes de verificar si termina en un punto.
# * Esto aseguraría que la verificación de la terminación en punto sea precisa.
# • ¿Qué otros caracteres de puntuación podrías considerar?
# * Respuesta: Además del punto, se podrían considerar otros caracteres de puntuación como el signo de exclamación (!), el signo de interrogación (?),
# * o incluso comas (,) dependiendo del contexto de la frase. Se podría usar una lista de caracteres de puntuación y verificar si la cadena termina
# * en alguno de ellos.

frase = input("Introduce una frase o palabra: ")
if not frase.endswith("."):
    frase += "."
print(frase)

# Ejercicio 8: Validador de contraseña segura
# Objetivo: Implementar múltiples condiciones.
# Instrucciones:
# 1. Pide al usuario que cree una contraseña.
# 2. Verifica que cumpla:
# o 8+ caracteres y ≤20 caracteres.
# o Al menos 1 mayúscula (usa .isupper()).
# o Al menos 1 número (usa .isdigit()).
# 3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
# 4. Si no, imprime: "La contraseña no es segura.".
# Preguntas de reflexión:
# • ¿Cómo añadirías la regla de usar un carácter especial?
# * Respuesta: Para añadir la regla de usar un carácter especial, se podría usar una lista
# * de caracteres especiales y verificar si la contraseña contiene al menos uno de ellos.
# * Esto se podría hacer usando el método any() y una comprensión de lista para verificar
# * si alguno de los caracteres especiales está presente en la contraseña.
# • ¿Por qué es importante limitar la longitud máxima?
# * Respuesta: Limitar la longitud máxima es importante porque contraseñas demasiado largas pueden ser difíciles de recordar y manejar.

password = input("Crea una contraseña: ")
if (
    (len(password) < 8 or len(password) > 20)
    and not any(c.isupper() for c in password)
    or not any(c.isdigit() for c in password)
):
    print("La contraseña no es segura.")
else:
    print("¡Felicitaciones! Creaste tu contraseña.")

# Ejercicio 9: Mejorando mensajes de error
# Objetivo: Dar retroalimentación específica al usuario.
# Instrucciones:
# 1. Basado en el Ejercicio 8, mejora los mensajes de error:
# o Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al
# menos 8 caracteres.".
# o Si tiene >20 caracteres: "...no más de 20 caracteres.".
# o Si falta mayúscula: "...al menos una mayúscula.".
# o Si falta número: "...al menos un número.".
# Preguntas de reflexión:
# • ¿Cómo evitarías repetir código al verificar cada condición?
# * Respuesta: Para evitar repetir código, se podría usar una lista de condiciones y un bucle para verificar cada condición.
# * Luego, se podría imprimir un mensaje de error específico para cada condición que no se cumpla.
# * Esto haría el código más limpio y fácil de mantener.
# • ¿Qué ventajas tiene este enfoque para el usuario?
# * Respuesta: Este enfoque tiene la ventaja de proporcionar retroalimentación específica al usuario sobre qué condiciones no se cumplen,
# * lo que facilita la corrección de la contraseña. Además, mejora la experiencia del usuario al hacer el proceso más claro y comprensible.

password = input("Crea una contraseña: ")
if len(password) < 8:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
elif len(password) > 20:
    print("La contraseña no debe tener más de 20 caracteres.")
elif not any(c.isupper() for c in password):
    print("La contraseña no es segura. Debe tener al menos una mayúscula.")
elif not any(c.isdigit() for c in password):
    print("La contraseña no es segura. Debe tener al menos un número.")
else:
    print("¡Felicitaciones! Creaste tu contraseña.")

# Ejercicio 10: Piedra, papel o tijera
# Objetivo: Implementar lógica de juego con condicionales anidados.
# Instrucciones:
# 1. Pide al usuario las jugadas del Jugador 1 y Jugador 2 (piedra, papel o tijera).
# 2. Usa la tabla proporcionada para determinar el resultado (ganador o
# empate).
# | Resultado      | Jugador 1 | Jugador 2 |
# |----------------|-----------|-----------|
# | EMPATE         | Piedra    | Piedra    |
# | GANA JUGADOR 2 | Piedra    | Papel     |
# | GANA JUGADOR 1 | Piedra    | Tijera    |
# | GANA JUGADOR 1 | Papel     | Piedra    |
# | EMPATE         | Papel     | Papel     |
# | GANA JUGADOR 2 | Papel     | Tijera    |
# | GANA JUGADOR 2 | Tijera    | Piedra    |
# | GANA JUGADOR 1 | Tijera    | Papel     |
# | EMPATE         | Tijera    | Tijera    |
# 3. Imprime: "GANA JUGADOR 1", "GANA JUGADOR 2" o "EMPATE".
# Preguntas de reflexión:
# • ¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?
# * Respuesta: Con else, se podría imprimir un mensaje de error indicando que la entrada es inválida y pedir al usuario que ingrese una opción válida.
# • ¿Qué estructura usarías para simplificar las comparaciones?
# * Respuesta: Se podría usar un diccionario para almacenar las jugadas y sus resultados, lo que haría el código más limpio y fácil de entender.
# Bonus:
# • Diagrama de flujo: Dibuja el diagrama de flujo del Ejercicio 10.

jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
if jugador1 == jugador2:
    print("EMPATE")
elif jugador1 == "piedra":
    if jugador2 == "papel":
        print("GANA JUGADOR 2")
    else:
        print("GANA JUGADOR 1")
elif jugador1 == "papel":
    if jugador2 == "piedra":
        print("GANA JUGADOR 1")
    else:
        print("GANA JUGADOR 2")
elif jugador1 == "tijera":
    if jugador2 == "piedra":
        print("GANA JUGADOR 2")
    else:
        print("GANA JUGADOR 1")

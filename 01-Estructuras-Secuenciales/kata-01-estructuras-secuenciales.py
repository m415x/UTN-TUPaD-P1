# Ejercicio 1: Cálculo del área y el perímetro de un rectángulo
# Objetivo: Calcular el área y el perímetro a partir de medidas dadas por el
# usuario.
# Instrucciones:
# 1. Pedir al usuario que ingrese el ancho y el alto de un rectángulo.
# 2. Calcular el área usando la fórmula: ancho * alto.
# 3. Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2).
# 4. Mostrar ambos resultados en pantalla.
# Preguntas de reflexión:
# • ¿Qué sucede si se ingresan valores negativos?
# * Respuesta: Si se ingresan valores negativos, el área y el perímetro no tendrían sentido físico.
# • ¿Podría adaptarse este cálculo a otras figuras geométricas?
# * Respuesta: Sí, se podría adaptar a otras figuras como triángulos o círculos, usando las fórmulas correspondientes.

ancho = float(input("Ingrese el ancho del rectángulo: "))
alto = float(input("Ingrese el alto del rectángulo: "))
area = ancho * alto
perimetro = (ancho * 2) + (alto * 2)
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")

# Ejercicio 2: Conversión de grados Celsius a Fahrenheit
# Objetivo: Realizar la conversión de temperatura de Celsius a Fahrenheit.
# Instrucciones:
# 1. Solicitar al usuario una temperatura en grados Celsius.
# 2. Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32.
# 3. Mostrar el resultado en pantalla.
# Preguntas de reflexión:
# • ¿Qué resultado se obtiene al ingresar 0°C?
# * Respuesta: Al ingresar 0°C, el resultado es 32°F.
# • ¿Cómo se adaptaría este ejercicio para convertir a Kelvin?
# * Respuesta: Para convertir a Kelvin, se puede usar la fórmula K = C + 273.15.

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit}")

# Ejercicio 3: Uso de booleanos
# Objetivo: Manipular variables booleanas y aplicar operadores lógicos.
# Instrucciones:
# 1. Declarar dos variables booleanas: a = True, b = False.
# 2. Realizar e imprimir los resultados de las operaciones:
# o a and b
# o a or b
# o not a, not b
# Preguntas de reflexión:
# • ¿Cuál es la utilidad de los operadores lógicos en programas más complejos?
# * Respuesta: Los operadores lógicos son útiles para tomar decisiones basadas en múltiples condiciones.
# • ¿Qué representa cada operación?
# * Respuesta: "and" devuelve True si ambas condiciones son verdaderas,
# * "or" devuelve True si al menos una es verdadera, y "not" invierte el valor booleano.

a = True
b = False
print(f"a and b: {a and b}")  # False
print(f"a or b: {a or b}")  # True
print(f"not a: {not a}")  # False
print(f"not b: {not b}")  # True

# Ejercicio 4: Prueba de escritorio
# Objetivo: Analizar el funcionamiento del código y predecir su resultado.
# Instrucciones:
# 1. Leer el siguiente código:
# a = 5
# b = 3
# c = a + b
# a = 2
# print(c)
# 2. Realizar una prueba de escritorio paso a paso.
# 3. Determinar qué imprime el programa y por qué.
# Preguntas de reflexión:
# • ¿Por qué el cambio en a no afecta al valor de c?
# * Respuesta: Porque c se calcula antes de cambiar el valor de a, y almacena el resultado de la suma.
# • ¿Qué pasa si se imprime a y b al final?
# * Respuesta: Si se imprime a y b al final, se mostraría 2 y 3 respectivamente, ya que a fue cambiado a 2.

a = 5
b = 3
c = a + b  # c = 8
a = 2
print(c)  # Imprime 8, ya que c se calcula antes de cambiar el valor de a.

# Ejercicio 5: Diagrama de flujo – Cuadrado de un número
# Objetivo: Representar visualmente un algoritmo sencillo.
# Instrucciones:
# 1. Dibujar un diagrama de flujo para un programa que:
# o Pide al usuario un número.
# o Calcula su cuadrado.
# o Muestra el resultado.
# 2. Implementar el programa en código si lo deseás.
# Preguntas de reflexión:
# • ¿Qué ventajas tiene el uso de diagramas de flujo?
# * Respuesta: Los diagramas de flujo ayudan a visualizar el proceso y a identificar errores lógicos antes de codificar.
# • ¿Cómo se representa una operación matemática en un diagrama?
# * Respuesta: Se representa con un rombo o un rectángulo, dependiendo de si es una operación o una decisión.

numero = int(input("Ingrese un número: "))
cuadrado = numero**2
print(f"El cuadrado de {numero} es: {cuadrado}")

# Ejercicio 6: Intercambio de variables
# Objetivo: Intercambiar valores sin usar una variable temporal.
# Instrucciones:
# 1. Declarar dos variables: x = 10, y = 20.
# 2. Intercambiar sus valores usando operaciones aritméticas.
# 3. Mostrar los valores antes y después del intercambio.
# Preguntas de reflexión:
# • ¿Cómo funciona el intercambio sin variable auxiliar?
# * Respuesta: Se usa la asignación múltiple de Python, que permite intercambiar valores sin necesidad de una variable temporal.
# • ¿Qué pasa si los valores iniciales son iguales?
# * Respuesta: Si los valores son iguales, el intercambio no cambiará nada, pero no generará error.

x = 10
y = 20
print(f"Antes del intercambio: x = {x}, y = {y}")
x, y = y, x  # Intercambio de valores
print(f"Después del intercambio: x = {x}, y = {y}")

# Ejercicio 7: Cálculo del IMC (Índice de Masa Corporal)
# Objetivo: Aplicar fórmulas con variables numéricas ingresadas por el usuario.
# Instrucciones:
# 1. Solicitar al usuario su peso en kg y su altura en metros.
# 2. Calcular el IMC con la fórmula: IMC = peso / (altura ** 2).
# 3. Mostrar el resultado con un mensaje como: "Tu IMC es: 22.5".
# Preguntas de reflexión:
# • ¿Qué rango se considera saludable para el IMC?
# * Respuesta: Un IMC entre 18.5 y 24.9 se considera saludable.
# • ¿Cómo podrías dar una recomendación según el resultado?
# * Respuesta: Se podría agregar una serie de condiciones para clasificar el IMC en bajo peso, normal, sobrepeso y obesidad.

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura**2)
print(f"Tu IMC es: {imc:.2f}")  # Muestra el IMC con 2 decimales

# Ejercicio 8: Contador de caracteres en un nombre
# Objetivo: Aplicar operaciones con cadenas de texto.
# Instrucciones:
# 1. Pedir al usuario que ingrese su nombre completo.
# 2. Calcular y mostrar:
# o La cantidad total de letras (sin contar espacios).
# o Las primeras 3 letras del nombre.
# o El nombre con letras en mayúsculas y minúsculas alternadas
# (ejemplo: "JuAn PeReZ").
# Preguntas de reflexión:
# • ¿Qué técnicas de manipulación de strings estás usando?
# * Respuesta: Se usan técnicas como el conteo de caracteres, el slicing para obtener
# * las primeras letras y la comprensión de listas para alternar mayúsculas y minúsculas.
# • ¿Cómo podrías extender este ejercicio para apellidos?
# * Respuesta: Se podría pedir al usuario que ingrese su apellido y aplicar las mismas técnicas.

nombre = input("Ingrese su nombre completo: ")
letras = len(nombre.replace(" ", ""))  # Cantidad de letras sin contar espacios
print(f"Cantidad total de letras: {letras}")
primeras_tres = nombre[:3]  # Primeras 3 letras del nombre
print(f"Las primeras 3 letras del nombre son: {primeras_tres}")

alternar = "".join(
    [c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(nombre)]
)  # Alternar mayúsculas y minúsculas
print(f"El nombre con letras alternadas es: {alternar}")

# Ejercicio 9: Operaciones con números flotantes
# Objetivo: Realizar distintas operaciones matemáticas con decimales.
# Instrucciones:
# 1. Declarar:
# o a = 7.5
# o b = 3.2
# 2. Calcular y mostrar:
# o La suma (a + b)
# o El redondeo de la división (a / b) a 2 decimales
# o La potencia (a ** b)
# Preguntas de reflexión:
# • ¿Qué ocurre si redondeás a más decimales?
# * Respuesta: Si redondeo a más decimales, el resultado será más preciso, pero puede ser menos legible.
# • ¿Cuándo conviene usar math.pow()?
# * Respuesta: Se recomienda usar math.pow() cuando se necesita una mayor precisión en cálculos matemáticos complejos.

a = 7.5
b = 3.2
suma = a + b
print(f"La suma de {a} y {b} es: {suma}")
division = a / b
print(f"La división de {a} entre {b} redondeada a 2 decimales es: {division:.2f}")
potencia = a**b  # Potencia
print(f"{a} elevado a {b} es: {potencia}")

# Ejercicio 10: Descuento sobre precio original
# Objetivo: Aplicar porcentajes y mostrar el resultado.
# Instrucciones:
# 1. Pedir al usuario el precio original de un producto.
# 2. Pedir el porcentaje de descuento.
# 3. Calcular el precio final:
# precio_final = precio_original * (1 - (descuento / 100))
# 4. Mostrar el precio con descuento.
# 5. (Opcional) Dibujar un diagrama de flujo del proceso.
# Preguntas de reflexión:
# • ¿Qué ocurre si el descuento es mayor a 100%?
# * Respuesta: Si el descuento es mayor a 100%, el precio final sería negativo, lo cual no tiene sentido.
# • ¿Cómo podrías mostrar el monto ahorrado?
# * Respuesta: Se podría calcular el monto ahorrado como: monto_ahorrado = precio_original - precio_final.

precio = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = precio * (1 - (descuento / 100))
print(f"El precio final con descuento es: {precio_final:.2f}")

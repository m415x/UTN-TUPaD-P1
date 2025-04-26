# === Importaciones ===

from math import pi
from utilidades.funciones import leer_entero_validado

# === Definición de funciones ===

# 1) Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.


def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' en la terminal."""
    print("Hola Mundo!")


# 2) Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá
# devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


def saludar_usuario(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola {nombre}!"


# 3) Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores
# ingresados.


def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime la información personal del usuario."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el
# radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro
# y devuelva el perímetro del círculo. Solicitar el radio al usuario
# y llamar ambas funciones para mostrar los resultados.


def calcular_area_circulo(radio):
    """Devuelve el área del círculo dado su radio."""
    return round(pi * radio**2, 2)


def calcular_perimetro_circulo(radio):
    """Devuelve el perímetro del círculo dado su radio."""
    return round(2 * pi * radio, 2)


# 5) Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y
# mostrar el resultado usando esta función.


def segundos_a_horas(segundos):
    """Devuelve la cantidad de horas correspondientes a una cantidad de segundos."""
    return round(int(segundos) / 3600)


# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la
# función.


def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del número dado."""
    numero = int(numero)

    print(f"Tabla de multiplicar del {numero}:")
    print("=======================================")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 7) Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los
# resultados de forma clara.


def operaciones_basicas(a, b):
    """Devuelve una tupla con los resultados de las operaciones básicas entre dos números."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"

    return suma, resta, multiplicacion, division


# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la
# función para mostrar el resultado con dos decimales.


def calcular_imc(peso, altura):
    """Devuelve el índice de masa corporal (IMC) a partir del peso y la altura."""
    return round(float(peso) / float(altura) ** 2, 2)


# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


def celsius_a_fahrenheit(celsius):
    """Devuelve la temperatura en grados Fahrenheit a partir de la temperatura en grados Celsius."""
    return round(float(celsius) * 9 / 5 + 32, 2)


# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


def calcular_promedio(a, b, c):
    """Devuelve el promedio de tres números."""
    return round((float(a) + float(b) + float(c)) / 3, 2)


# === Programa principal ===

if __name__ == "__main__":
    # Solicitar al usuario que elija una opción del menú.
    opcion = leer_entero_validado("Elija un ejercicio (1 al 10) para ejecutar", 1, 10)

    match opcion:
        case 1:
            # Llamar a la función imprimir_hola_mundo.
            imprimir_hola_mundo()

        case 2:
            nombre = input("Ingresa tu nombre: ")

            # Llamar a la función saludar_usuario con el nombre ingresado por el usuario e imprimir
            # por terminal el retorno de la función.
            print(saludar_usuario(nombre))

        case 3:
            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")
            edad = input("Ingresa tu edad: ")
            residencia = input("Ingresa tu lugar de residencia: ")

            # Llamar a la función informacion_personal con los datos ingresados por el usuario.
            informacion_personal(nombre, apellido, edad, residencia)

        case 4:
            radio = float(input("Ingresa el radio del círculo: "))

            # Llamar a la función calcular_area_circulo con el radio ingresado por el usuario e imprimir
            # por terminal el retorno de la función.
            print(f"El área del círculo es: {calcular_area_circulo(radio)}")

            # Llamar a la función calcular_perimetro_circulo con el radio ingresado por el usuario e
            # imprimir por terminal el retorno de la función.
            print(f"El perímetro del círulo es {calcular_perimetro_circulo(radio)}")

        case 5:
            segundos = int(input("Ingresa la cantidad de segundos: "))

            # Llamar a la función segundos_a_horas con los segundos ingresados por el usuario e imprimir
            # por terminal el retorno de la función.
            print(f"Equivale a {segundos_a_horas(segundos)} horas")

        case 6:
            numero = input("Ingresa un número: ")

            # Llamar a la función tabla_multiplicar con el número ingresado por el usuario.
            tabla_multiplicar(numero)

        case 7:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))

            # Llamar a la función operaciones_basicas con los números ingresados por el usuario e imprimir
            # por terminal el retorno de la función.
            operaciones = operaciones_basicas(a, b)

            print("Resultados de las operaciones básicas:")
            print(
                f"""
                    Suma: {a} + {b} = {operaciones[0]}
                    Resta: {a} - {b} = {operaciones[1]}
                    Multiplicación: {a} * {b} = {operaciones[2]}
                    División: {a} / {b} = {operaciones[3]}
                """
            )

        case 8:
            peso = input("Ingresa tu peso en kg: ")
            altura = input("Ingresa tu altura en metros: ")

            # Llamar a la función calcular_imc con los datos ingresados por el usuario e imprimir
            # por terminal el retorno de la función.
            print(f"El IMC es: {calcular_imc(peso, altura)}")

        case 9:
            celsius = input("Ingresa la temperatura en grados Celsius: ")

            # Llamar a la función celsius_a_fahrenheit con la temperatura ingresada por el usuario e imprimir
            # por terminal el retorno de la función.
            print(f"La temperatura equivalente es {celsius_a_fahrenheit(celsius)}°F")

        case 10:
            a = input("Ingresa el primer número: ")
            b = input("Ingresa el segundo número: ")
            c = input("Ingresa el tercer número: ")

            # Llamar a la función calcular_promedio con los números ingresados por el usuario e imprimir
            # por terminal el retorno de la función.
            print(f"El promedio es: {calcular_promedio(a, b, c)}")

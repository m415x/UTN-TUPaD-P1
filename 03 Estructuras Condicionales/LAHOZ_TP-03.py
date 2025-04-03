from random import randint
from statistics import mode, median, mean

opcion = input("Elija un ejercicio (1 al 10) para ejecutar: ")

match opcion:
    case "1":
        # Escribir un programa que solicite la edad del usuario.
        # Si el usuario es mayor de 18 años, deberá mostrar un
        # mensaje en pantalla que diga “Es mayor de edad”.

        edad = int(input("Ingrese su edad: "))

        if edad > 18:
            print("Es mayor de edad")

    case "2":
        # Escribir un programa que solicite su nota al usuario.
        # Si la nota es mayor o igual a 6, deberá mostrar por
        # pantalla un mensaje que diga “Aprobado”; en caso
        # contrario deberá mostrar el mensaje “Desaprobado”.

        nota = float(input("Ingrese su nota: "))

        if nota >= 6:
            print("Aprobado")
        else:
            print("Desaprobado")

    case "3":
        # Escribir un programa que permita ingresar solo números pares.
        # Si el usuario ingresa un número par, imprimir por en
        # pantalla el mensaje "Ha ingresado un número par"; en caso
        # contrario, imprimir por pantalla "Por favor, ingrese un
        # número par". Nota: investigar el uso del operador de módulo
        # (%) en Python para evaluar si un número es par o impar.

        numero = int(input("Ingrese un número par: "))

        if numero % 2 == 0:
            print("Ha ingresado un número par")
        else:
            print("Por favor, ingrese un número par")

    case "4":
        # Escribir un programa que solicite al usuario su edad e imprima
        # por pantalla a cuál de las siguientes categorías pertenece:
        #   ● Niño/a: menor de 12 años.
        #   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
        #   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
        #   ● Adulto/a: mayor o igual que 30 años.

        edad = int(input("Ingrese su edad: "))

        if edad < 12:
            print("Niño/a")
        elif 12 <= edad < 18:
            print("Adolescente")
        elif 18 <= edad < 30:
            print("Adulto/a joven")
        else:
            print("Adulto/a")

    case "5":
        # Escribir un programa que permita introducir contraseñas de
        # entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario
        # ingresa una contraseña de longitud adecuada, imprimir por en
        # pantalla el mensaje "Ha ingresado una contraseña correcta";
        # en caso contrario, imprimir por pantalla "Por favor, ingrese
        # una contraseña de entre 8 y 14 caracteres". Nota: investigue
        # el uso de la función len() en Python para evaluar la cantidad
        # de elementos que tiene un iterable tal como una lista o un string.

        password = len(input("Ingrese una contraseña de entre 8 y 14 caracteres: "))

        if 8 <= password <= 14:
            print("Ha ingresado una contraseña correcta")
        else:
            print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

    case "6":
        # El paquete statistics de python contiene funciones que permiten
        # tomar una lista de números y calcular la moda, la mediana y la
        # media de dichos números. Un ejemplo de su uso es el siguiente:
        # *  from statistics import mode, median, mean
        # *  mi_lista = [1,2,5,5,3]
        # *  mean(mi_lista)
        # En la documentación oficial se puede encontrar más información
        # sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html.
        # La moda (mode), la mediana (median) y la media (mean) son parámetros
        # estadísticos que se pueden utilizar para predecir la forma de
        # una distribución normal a partir del siguiente criterio:
        #   ● Sesgo positivo o a la derecha: cuando la media es mayor que
        #     la mediana y, a su vez, la mediana es mayor que la moda.
        #   ● Sesgo negativo o a la izquierda: cuando la media es menor
        #     que la mediana y, a su vez, la mediana es menor que la moda.
        #   ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
        # Teniendo en cuenta lo antes mencionado, escribir un programa que
        # tome la lista numeros_aleatorios, calcule su moda, su mediana y
        # su media y las compare para determinar si hay sesgo positivo, negativo
        # o no hay sesgo. Imprimir el resultado por pantalla.
        # Definir la lista numeros_aleatorios de la siguiente forma:
        # *  import random
        # *  numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
        # Nota: el bloque de código anterior crea una lista con 50 números entre
        # 1 y 100 elegidos de forma aleatoria.

        numeros_aleatorios = [randint(1, 100) for i in range(50)]
        moda = mode(numeros_aleatorios)
        mediana = median(numeros_aleatorios)
        media = mean(numeros_aleatorios)

        if media > mediana > moda:
            print("Sesgo positivo")
        elif media < mediana < moda:
            print("Sesgo negativo")
        else:
            print("No hay sesgo")

    case "7":
        # Escribir un programa que solicite una frase o palabra al usuario.
        # Si el string ingresado termina con vocal, añadir un signo de
        # exclamación al final e imprimir el string resultante por pantalla;
        # en caso contrario, dejar el string tal cual lo ingresó el usuario
        # e imprimirlo por pantalla.

        frase = input("Escriba una frase: ")

        if frase[-1].lower() in "aeiou":
            print(frase := frase + "!")
        else:
            print(frase)

    case "8":
        # Escribir un programa que solicite al usuario que ingrese su
        # nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
        #   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
        #   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
        #   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
        # El programa debe transformar el nombre ingresado de acuerdo a
        # la opción seleccionada por el usuario e imprimir el resultado
        # por pantalla. Nota: investigue uso de las funciones upper(),
        # lower() y title() de Python para convertir entre mayúsculas
        # y minúsculas.

        nombre = input("Ingrese su nombre: ")
        opcion = input("""
                Ingrese el número  de la opción que desee: 
                1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
                2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
                3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
            """)

        if opcion == "1":
            print(nombre := nombre.upper())
        elif opcion == "2":
            print(nombre := nombre.lower())
        elif opcion == "3":
            print(nombre := nombre.title())
        else:
            print("Opción incorrecta")

    case "9":
        # Escribir un programa que pida al usuario la magnitud de un terremoto,
        # clasifique la magnitud en una de las siguientes categorías según la
        # escala de Richter e imprima el resultado por pantalla:
        #   ● Menor que 3: "Muy leve" (imperceptible).
        #   ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible).
        #   ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero
        #     generalmente no causa daños).
        #   ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras
        #     débiles).
        #   ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos).
        #   ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

        magnitud = float(input("Ingrese la magnitud del terremoto: "))

        if magnitud < 3:
            print('"Muy leve" (imperceptible)')
        elif 3 <= magnitud < 4:
            print('"Leve" (ligeramente perceptible)')
        elif 4 <= magnitud < 5:
            print('"Moderado" (sentido por personas, pero generalmente no causa daños)')
        elif 5 <= magnitud < 6:
            print('"Fuerte" (puede causar daños en estructuras débiles)')
        elif 6 <= magnitud < 7:
            print('"Muy Fuerte" (puede causar daños significativos)')
        else:
            print('"Extremo" (puede causar graves daños a gran escala)')

    case "10":
        # Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
        #
        # ! ------------------------------- | ---------------- | ---------------- |
        # !         Periodo del año         |  Estación en el  |  Estación en el  |
        # !                                 | hemisferio norte |  hemisferio sur  |
        # ! :-----------------------------: | :--------------: | :--------------: |
        # ! Desde el 21 de diciembre hasta  |                  |                  |
        # ! el 20 de marzo (incluidos)      |     Invierno     |      Verano      |
        # ! ------------------------------- | ---------------- | ---------------- |
        # ! Desde el 21 de marzo hasta      |                  |                  |
        # ! el 20 de junio (incluidos)      |     Primavera    |       Otoño      |
        # ! ------------------------------- | ---------------- | ---------------- |
        # ! Desde el 21 de junio hasta      |                  |                  |
        # ! el 20 de septiembre (incluidos) |      Verano      |     Invierno     |
        # ! ------------------------------- | ---------------- | ---------------- |
        # ! Desde el 21 de septiembre hasta |                  |                  |
        # ! el 20 de diciembre (incluidos)  |       Otoño      |     Primavera    |
        # ! ------------------------------- | ---------------- | ---------------- |
        #
        # Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
        # qué mes del año es y qué día es. El programa deberá utilizar esa información para
        # imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

        # Solicitar datos al usuario
        hemisferio = input(
            "¿En qué hemisferio estás? (N para Norte, S para Sur): "
        ).upper()
        mes = input("¿Qué mes es? (ej. enero, febrero, etc.): ").lower()
        dia = int(input("¿Qué día es? (1-31): "))

        # Convertir mes a número (1-12)
        if mes == "enero":
            mes_num = 1
        elif mes == "febrero":
            mes_num = 2
        elif mes == "marzo":
            mes_num = 3
        elif mes == "abril":
            mes_num = 4
        elif mes == "mayo":
            mes_num = 5
        elif mes == "junio":
            mes_num = 6
        elif mes == "julio":
            mes_num = 7
        elif mes == "agosto":
            mes_num = 8
        elif mes == "septiembre":
            mes_num = 9
        elif mes == "octubre":
            mes_num = 10
        elif mes == "noviembre":
            mes_num = 11
        elif mes == "diciembre":
            mes_num = 12
        else:
            print("Mes no válido")
            exit()

        # Determinar estación para hemisferio norte
        if hemisferio == "N":
            if (
                (mes_num == 12 and dia >= 21)
                or (mes_num == 1)
                or (mes_num == 2)
                or (mes_num == 3 and dia <= 20)
            ):
                print("Estás en Invierno")
            elif (
                (mes_num == 3 and dia >= 21)
                or (mes_num == 4)
                or (mes_num == 5)
                or (mes_num == 6 and dia <= 20)
            ):
                print("Estás en Primavera")
            elif (
                (mes_num == 6 and dia >= 21)
                or (mes_num == 7)
                or (mes_num == 8)
                or (mes_num == 9 and dia <= 20)
            ):
                print("Estás en Verano")
            elif (
                (mes_num == 9 and dia >= 21)
                or (mes_num == 10)
                or (mes_num == 11)
                or (mes_num == 12 and dia <= 20)
            ):
                print("Estás en Otoño")
            else:
                print("Fecha no válida")

        # Determinar estación para hemisferio sur
        elif hemisferio == "S":
            if (
                (mes_num == 12 and dia >= 21)
                or (mes_num == 1)
                or (mes_num == 2)
                or (mes_num == 3 and dia <= 20)
            ):
                print("Estás en Verano")
            elif (
                (mes_num == 3 and dia >= 21)
                or (mes_num == 4)
                or (mes_num == 5)
                or (mes_num == 6 and dia <= 20)
            ):
                print("Estás en Otoño")
            elif (
                (mes_num == 6 and dia >= 21)
                or (mes_num == 7)
                or (mes_num == 8)
                or (mes_num == 9 and dia <= 20)
            ):
                print("Estás en Invierno")
            elif (
                (mes_num == 9 and dia >= 21)
                or (mes_num == 10)
                or (mes_num == 11)
                or (mes_num == 12 and dia <= 20)
            ):
                print("Estás en Primavera")
            else:
                print("Fecha no válida")

        else:
            print("Hemisferio no válido. Debe ser N o S.")

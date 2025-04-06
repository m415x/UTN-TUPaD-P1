from random import randint

opcion = input(
    "Elija un ejercicio (1 al 10) para ejecutar o escriba 'salir' para finalizar: "
)

while opcion != "salir":
    opcion = input(
        "Elija un ejercicio (1 al 10) para ejecutar o escriba 'salir' para finalizar: "
    )

    match opcion:
        case "1":
            # Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
            # (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

            for i in range(101):
                print(i)

        case "2":
            # Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
            # dígitos que contiene.

            # ** Con Bucle WHILE**
            numero = aux = int(input("Ingrese un número entero: "))
            cont = 0

            while aux != 0:
                aux //= 10
                cont += 1

            print(f"La cantidad de dígitos de {numero} es: {cont}")

            # ** Sin Bucle **
            # numero = input("Ingrese un número entero: ")
            # print(f"La cantidad de dígitos de {numero} es: {len(numero)}")

        case "3":
            # Escribe un programa que sume todos los números enteros comprendidos entre dos valores
            # dados por el usuario, excluyendo esos dos valores.

            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            suma = 0

            for i in range(
                num1 + 1 if num1 <= num2 else num2 + 1,
                num2 if num1 <= num2 else num1,
                1,
            ):
                suma += i

            print(
                f"La suma de los enteros comprendidos entre {num1} y {num2}, excluyendo estos, es: {suma}"
            )

        case "4":
            # Elabora un programa que permita al usuario ingresar números enteros y los sume en
            # secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
            # un 0.

            numero = 1
            suma = 0

            while numero != 0:
                numero = int(input("Ingrese un número entero (0 para finalizar): "))
                suma += numero

            print("El total acumulado es: ", suma)

        case "5":
            # Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
            # programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

            numero_aleatorio = randint(0, 9)
            numero = -1
            intento = 0

            while numero != numero_aleatorio:
                numero = int(input("Ingrese un número entero entre 0 y 9: "))
                intento += 1

            print(f"Adivinó el número {numero_aleatorio} en {intento} intentos")

        case "6":
            # Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
            # entre 0 y 100, en orden decreciente.

            for num in range(100, -1, -2):
                print(num)

        case "7":
            # Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
            # número entero positivo indicado por el usuario.

            numero = int(input("Ingrese un número entero positivo: "))
            suma = 0

            for num in range(0, numero + 1):
                suma += num

            print(f"La suma de los enteros entre 0 y {numero} es: {suma}")

        case "8":
            # Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
            # programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
            # negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
            # menor, pero debe estar preparado para procesar 100 números con un solo cambio).

            cont_par = 0
            cont_imp = 0
            cont_pos = 0
            cont_neg = 0

            for i in range(1, 101):
                numero = int(input(f"Ingrese el {i}° número entero: "))

                if numero % 2 == 0:
                    cont_par += 1
                else:
                    cont_imp += 1

                if numero >= 0:
                    cont_pos += 1
                else:
                    cont_neg += 1

            print(f"""
    Números pares: {cont_par}
    Números impares: {cont_imp}
    Números positivos: {cont_pos}
    Números negativos: {cont_neg}
                """)

        case "9":
            # Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
            # media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
            # poder procesar 100 números cambiando solo un valor).

            suma = 0
            cont = 0

            for i in range(1, 101):
                numero = int(input(f"Ingrese el {i}° número entero: "))

                suma += numero
                cont = i

            print(f"La media de los {cont} valores es {suma / cont}")

        case "10":
            # Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
            # usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

            # ** Con Bucle FOR **
            numero = aux1 = int(input("Ingrese un número entero positivo: "))
            numero_invertido = 0

            for i in range(len(str(aux1)) - 1, -1, -1):
                aux2 = aux1 % 10
                aux1 //= 10
                numero_invertido += aux2 * 10**i

            print(f"El número {numero} invertido es {numero_invertido}")

            # ** Sin Bucle **
            # numero = input("Ingrese un número entero positivo: ")
            # print(f"El número {numero} invertido es {numero[::-1]}")

        case "salir":
            print("Saliendo del programa...")
            pass

        case _:
            print(
                "Opción no válida. Por favor, elija un número entre 1 y 10 o escriba 'salir'."
            )

# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# Diccionario inicial de precios de frutas
precios_frutas: dict[str, int] = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450,
}


def ejercicio_1() -> None:
    """
    Función para ejecutar el ejercicio 1 del diccionario de precios de frutas.
    Permite añadir nuevas frutas y sus precios a un diccionario existente.
    :param None:
    :return: None
    """

    # Declarar el diccionario global para poder modificarlo
    global precios_frutas

    # Imprimir el diccionario inicial
    print("Diccionario inicial de precios de frutas:")
    print(precios_frutas)

    # Añadiendo nuevas frutas y precios
    precios_frutas["Naranja"] = 1200
    precios_frutas["Manzana"] = 1500
    precios_frutas["Pera"] = 2300

    # Imprimir el diccionario actualizado
    print("\nDiccionario actualizado con nuevas frutas:")
    print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800


def ejercicio_2() -> None:
    """
    Función para ejecutar el ejercicio 2 del diccionario de precios de frutas.
    Permite actualizar los precios de algunas frutas en un diccionario existente.
    :param None:
    :return: None
    """

    # Llamar a la función del ejercicio 1 para inicializar el diccionario
    ejercicio_1()

    # Usar el diccionario global
    global precios_frutas

    # Actualizando precios de frutas
    precios_frutas["Banana"] = 1330
    precios_frutas["Manzana"] = 1700
    precios_frutas["Melón"] = 2800

    # Imprimir el diccionario actualizado con los nuevos precios
    print("\nDiccionario actualizado con los nuevos precios:")
    print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.


def ejercicio_3() -> None:
    """
    Función para ejecutar el ejercicio 3 del diccionario de precios de frutas.
    Permite crear una lista que contenga únicamente las frutas (claves) del diccionario de precios.
    :param None:
    :return: None
    """

    # Llamar a la función del ejercicio 2 para inicializar el diccionario
    ejercicio_2()

    # Usar el diccionario global
    global precios_frutas

    # Creando una lista de frutas a partir de las claves del diccionario precios_frutas
    lista_frutas: list[str] = list(precios_frutas.keys())

    # Imprimir la lista de frutas
    print("\nLista de frutas:")
    print(lista_frutas)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.


def ingresar_contactos() -> dict:
    """
    Función para ingresar contactos a la agenda telefónica.
    Permite al usuario ingresar 5 contactos con nombre y número de teléfono.
    :param None:
    :return: dict - Un diccionario con los contactos ingresados.
    """

    # Inicializando un diccionario para almacenar los contactos
    numeros_telefono: dict[str, int] = dict()

    print("\nBienvenido a la agenda telefónica")
    print("Por favor, ingrese los contactos a continuación:")

    # Permitiendo al usuario ingresar 5 contactos
    for i in range(5):
        print(f"\nIngrese el contacto {i + 1}")

        # Solicitar nombre y número de teléfono
        nombre: str = input("Nombre -> ").lower()
        numero: str = input("Teléfono -> ")

        # Validar que el nombre no esté vacío y que el número sea un dígito
        while not nombre or not numero.isdigit():
            print(
                "\nError: El nombre no puede estar vacío y el número debe ser un dígito."
            )
            nombre = input("Nombre -> ").lower()
            numero = input("Teléfono -> ")

        # Almacenar el contacto en el diccionario
        numeros_telefono[nombre] = int(numero)

    return numeros_telefono


def buscar_contacto(numeros_telefono: dict[str, int], nombre: str) -> str:
    """
    Función para buscar un contacto en la agenda telefónica.
    :param numeros_telefono: dict - Un diccionario con los contactos.
    :param nombre: str - El nombre del contacto a buscar.
    :return: str - El número de teléfono del contacto buscado o None si no existe.
    """

    return numeros_telefono.get(nombre, None)


def ejercicio_4() -> None:
    """
    Función para ejecutar el ejercicio 4 de la agenda telefónica.
    Permite ingresar contactos y buscar un contacto por nombre.
    :param None:
    :return: None
    """

    # Llamar a la función para ingresar contactos
    numeros_telefono: dict[str, int] = ingresar_contactos()

    nombre_alumno: str = input(
        "\nEscriba el nombre del contacto que desea buscar -> "
    ).lower()

    # Validar que el contacto exista en el diccionario
    while nombre_alumno not in numeros_telefono.keys():
        print("\nError: Ese contacto no se encuentra almacenado\n")
        nombre_alumno = input(
            "Escriba el nombre del contacto que desea buscar -> "
        ).lower()

    # Buscar el contacto en el diccionario
    numero_telefono: str = buscar_contacto(numeros_telefono, nombre_alumno)

    # Imprimir el número de teléfono del contacto buscado
    print(f"\nEl número de teléfono es -> {numero_telefono}")


# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.


def ejercicio_5() -> None:
    """
    Función para ejecutar el ejercicio 5 del contador de palabras.
    Permite al usuario ingresar una frase y muestra las palabras únicas y un diccionario
    con la cantidad de veces que aparece cada palabra.
    :param None:
    :return: None
    """

    print("\nBienvenido al contador de palabras")

    # Solicitar una frase al usuario
    frase: str = input("Ingrese una frase -> ")

    # Crear una lista de palabras a partir de la frase ingresada
    lista_frase: list[str] = frase.split(" ")

    # Imprimir la lista de palabras
    print("\nLista de palabras:")
    print(lista_frase)

    # Usar un set para obtener las palabras únicas
    set_frase: set[str] = set(lista_frase)

    # Imprimir las palabras únicas
    print("\nPalabras únicas (usando un set):")
    print(set_frase)

    # Crear un diccionario que cuente la cantidad de veces que aparece cada palabra
    diccionario_frase: dict[str, int] = {}

    # Crear un diccionario con la cantidad de veces que aparece cada palabra
    for palabra in set_frase:
        diccionario_frase[palabra] = lista_frase.count(palabra)

    # Imprimir el diccionario con la cantidad de veces que aparece cada palabra
    print("\nDiccionario con la cantidad de veces que aparece cada palabra:")
    print(diccionario_frase)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.


def ejercicio_6() -> None:
    """
    Función para ejecutar el ejercicio 6 del sistema de notas de alumnos.
    Permite ingresar los nombres de 3 alumnos y sus respectivas notas, y muestra el promedio de cada alumno.
    :param None:
    :return: None
    """

    print("\nBienvenido al sistema de notas de alumnos")

    # Inicializar un diccionario para almacenar las notas de los alumnos
    notas_alumnos: dict[str, tuple[float]] = {}

    # Permitir al usuario ingresar los datos de 3 alumnos
    for i in range(3):
        print(f"\nIngrese los datos del alumno {i + 1}")

        # Solicitar el nombre del alumno
        nombre_alumno: str = input("Nombre del alumno -> ").lower()

        # Lista para almacenar las notas del alumno
        notas: list[float] = []

        print("Ingrese las 3 notas del alumno:")

        # Permitir al usuario ingresar 3 notas para el alumno
        for j in range(3):
            # Solicitar la nota
            nota: float = float(input(f"Nota {j + 1} -> "))

            # Validar que la nota esté en el rango de 0 a 10
            while nota < 0 or nota > 10:
                print("Error: La nota debe estar entre 0 y 10.")
                nota = float(input(f"Nota {j + 1} -> "))

            # Almacenar la nota en la lista
            notas.append(nota)

        # Almacenar las notas del alumno en el diccionario
        notas_alumnos[nombre_alumno] = set(notas)

    print("\nPromedio de notas de los alumnos ingresados:\n")

    # Imprimir las notas de cada alumno
    for nombre_alumno, notas in notas_alumnos.items():
        # Calcular el promedio de las notas
        promedio: float = sum(notas) / len(notas)

        # Imprimir el nombre del alumno y sus notas
        print(f"Alumno: {nombre_alumno.capitalize()} - Promedio: {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


def ejercicio_7() -> None:
    """
    Función para ejecutar el ejercicio 7 de estudiantes aprobados.
    Permite ingresar dos sets de números representando estudiantes que aprobaron dos parciales
    y muestra los resultados solicitados.
    :param None:
    :return: None
    """
    print("\nBienvenido al sistema de estudiantes")

    # Inicializar los sets de estudiantes que aprobaron los parciales
    parcial_1: set[int] = {1, 2, 3, 4, 5}
    parcial_2: set[int] = {4, 5, 6, 7, 8}

    print("Estudiantes que aprobaron Parcial 1:", parcial_1)
    print("Estudiantes que aprobaron Parcial 2:", parcial_2)

    # Estudiantes que aprobaron ambos parciales
    aprobados_ambos: set[int] = parcial_1.intersection(parcial_2)
    print("\nEstudiantes que aprobaron ambos parciales:", aprobados_ambos)

    # Estudiantes que aprobaron solo uno de los dos parciales
    aprobados_solo_uno: set[int] = parcial_1.symmetric_difference(parcial_2)
    print(
        "Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno
    )

    # Lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
    total_aprobados: set[int] = parcial_1.union(parcial_2)
    print(
        "Lista total de estudiantes que aprobaron al menos un parcial:", total_aprobados
    )


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.


class Productos:
    """
    Clase para gestionar un diccionario de productos y su stock.
    Permite consultar el stock de un producto, agregar unidades al stock de un producto existente
    y agregar un nuevo producto al diccionario.
    """

    def __init__(self) -> None:
        """
        Inicializa el diccionario de productos con sus respectivos stocks.
        """

        # Diccionario de productos con su stock inicial
        self.productos: dict[str, int] = {
            "televisores": 15,
            "celulares": 20,
            "heladeras": 3,
            "lavarropas": 8,
        }

    def consultar_stock(self, producto: str) -> int:
        """
        Consultar el stock de un producto.
        :param producto: str - Nombre del producto a consultar.
        :return: int - Stock del producto o 0 si no existe.
        """

        return self.productos.get(producto, 0)

    def agregar_stock(self, producto: str, unidades: int) -> None:
        """
        Agregar unidades al stock de un producto existente.
        Si el producto no existe, se agrega como un nuevo producto con las unidades especificadas.
        :param producto: str - Nombre del producto a agregar stock.
        :param unidades: int - Cantidad de unidades a agregar al stock.
        :return: None
        """

        # Comprobar si el producto ya existe en el diccionario
        if producto in self.productos:
            # Si existe, se suman las unidades al stock existente
            self.productos[producto] += unidades
        else:
            # Si no existe, se agrega el producto con las unidades especificadas
            self.productos[producto] = unidades


def ejercicio_8() -> None:
    """
    Función para ejecutar el ejercicio 8 del sistema de gestión de productos.
    Permite consultar el stock de un producto, agregar unidades al stock de un producto existente
    y agregar un nuevo producto al diccionario.
    :param None:
    :return: None
    """

    # Crear una instancia de la clase Productos
    gestion_productos: Productos = Productos()

    print("\nBienvenido al sistema de gestión de productos")

    # Bucle para mostrar las opciones al usuario
    while True:
        print("\nOpciones:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades al stock de un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Salir")

        # Solicitar al usuario que seleccione una opción
        opcion: int = int(input("Seleccione una opción (1-4) -> "))

        if opcion == 1:
            # Solicitar el nombre del producto a consultar
            producto: str = input(
                "Ingrese el nombre del producto a consultar -> "
            ).lower()

            # Consultar el stock del producto ingresado
            stock: int = gestion_productos.consultar_stock(producto)

            # Imprimir el stock del producto o un mensaje si no existe o no tiene stock
            if stock > 0:
                print(f"El stock del producto '{producto}' es: {stock} unidades.")
            else:
                print(f"El producto '{producto}' no existe o no tiene stock.")

        elif opcion == 2:
            # Solicitar el nombre del producto y las unidades a agregar
            producto: str = input(
                "Ingrese el nombre del producto a actualizar -> "
            ).lower()
            unidades: int = int(input("Ingrese la cantidad de unidades a agregar -> "))

            # Agregar las unidades al stock del producto
            gestion_productos.agregar_stock(producto, unidades)

            # Mostrar un mensaje de confirmación
            print(f"Se han agregado {unidades} unidades al producto '{producto}'.")
            print(
                f"El nuevo stock del producto '{producto}' es: {gestion_productos.consultar_stock(producto)} unidades."
            )

        elif opcion == 3:
            # Solicitar el nombre del nuevo producto y las unidades iniciales
            producto: str = input("Ingrese el nombre del nuevo producto -> ").lower()
            unidades: int = int(input("Ingrese la cantidad inicial de unidades -> "))

            # Agregar el nuevo producto al diccionario con las unidades especificadas
            # y mostrar un mensaje de confirmación
            gestion_productos.agregar_stock(producto, unidades)
            print(
                f"El nuevo producto '{producto}' ha sido agregado con {unidades} unidades."
            )

        elif opcion == 4:
            # Salir del programa
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.


class Agenda:
    """
    Clase para gestionar una agenda de eventos.
    Permite agregar eventos a la agenda y consultar qué actividad hay en cierto día y hora.
    """

    def __init__(self) -> None:
        """
        Inicializa un diccionario para almacenar los eventos en la agenda.
        Las claves son tuplas de (día, hora) y los valores son los eventos.
        """

        self.agenda: dict[tuple[int, str], str] = {}

    def agregar_evento(self, dia: int, hora: str, evento: str) -> None:
        """
        Agregar un evento a la agenda.
        :param dia: int - Día del evento.
        :param hora: str - Hora del evento.
        :param evento: str - Descripción del evento.
        :return: None
        """

        self.agenda[(dia, hora)] = evento

    def consultar_evento(self, dia: int, hora: str) -> str:
        """
        Consultar qué actividad hay en cierto día y hora.
        :param dia: int - Día del evento a consultar.
        :param hora: str - Hora del evento a consultar.
        :return: str - Descripción del evento o un mensaje si no hay actividad.
        """

        return self.agenda.get((dia, hora), "No hay actividad programada en la agenda.")


def ejercicio_9() -> None:
    """
    Función para ejecutar el ejercicio 9 de la agenda de eventos.
    Permite agregar eventos a la agenda y consultar qué actividad hay en cierto día y hora.
    :param None:
    :return: None
    """

    # Crear una instancia de la clase Agenda
    agenda: Agenda = Agenda()

    print("\nBienvenido a la agenda de eventos")

    # Bucle para mostrar las opciones al usuario
    while True:
        print("\nOpciones:")
        print("1. Agregar un evento")
        print("2. Consultar un evento")
        print("3. Salir")

        # Solicitar al usuario que seleccione una opción
        opcion: int = int(input("Seleccione una opción (1-3) -> "))

        if opcion == 1:
            # Solicitar los datos del evento
            dia: int = int(input("Ingrese el día del evento (1-31) -> "))
            hora: str = input("Ingrese la hora del evento (HH:MM) -> ")
            evento: str = input("Ingrese la descripción del evento -> ")

            # Agregar el evento a la agenda
            agenda.agregar_evento(dia, hora, evento)
            print(f"'{evento}' agregado para el día {dia} a las {hora}.")

        elif opcion == 2:
            # Solicitar los datos del evento a consultar
            dia: int = int(input("Ingrese el día del evento a consultar (1-31) -> "))
            hora: str = input("Ingrese la hora del evento a consultar (HH:MM) -> ")

            # Consultar el evento en la agenda
            resultado: str = agenda.consultar_evento(dia, hora)
            print(f"'{resultado}' programado para el día {dia} a las {hora}")

        elif opcion == 3:
            # Salir del programa
            print("Saliendo de la agenda...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.


class Paises:
    """
    Clase para gestionar un diccionario de países y sus capitales.
    Permite crear un nuevo diccionario donde las capitales son las claves y los países son los valores.
    """

    def __init__(self) -> None:
        """
        Inicializa un diccionario de países y sus capitales.
        """

        self.paises: dict[str, str] = {
            "Argentina": "Buenos Aires",
            "España": "Madrid",
            "Francia": "París",
            "Italia": "Roma",
            "Alemania": "Berlín",
        }

    def invertir_diccionario(self) -> dict[str, str]:
        """
        Invertir el diccionario de países y capitales.
        :return: dict - Un nuevo diccionario con las capitales como claves y los países como valores.
        """

        return {v: k for k, v in self.paises.items()}


def ejercicio_10() -> None:
    """
    Función para ejecutar el ejercicio 10 del diccionario de países y capitales.
    Permite invertir un diccionario donde las capitales son las claves y los países son los valores.
    :param None:
    :return: None
    """

    print("\nBienvenido al sistema de países y capitales")

    # Crear una instancia de la clase Paises
    gestion_paises: Paises = Paises()

    # Invertir el diccionario de países y capitales
    paises_invertidos: dict[str, str] = gestion_paises.invertir_diccionario()

    print("Diccionario original de países y capitales:")
    print(gestion_paises.paises)

    # Imprimir el nuevo diccionario con las capitales como claves y los países como valores
    print(
        "\nNuevo diccionario con las capitales como claves y los países como valores:"
    )
    print(paises_invertidos)


# Funciones para ejecutar los ejercicios
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
# ejercicio_5()
# ejercicio_6()
# ejercicio_7()
# ejercicio_8()
# ejercicio_9()
# ejercicio_10()

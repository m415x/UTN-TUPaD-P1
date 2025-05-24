# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def fact(num: int) -> int:
    """
    Calcula el factorial de un número de forma recursiva.
    :param num: int - Número entero positivo
    :return: int - Factorial del número
    """
    if num == 1:
        # Caso base: el factorial de 1 es 1
        return 1
    else:
        # Caso recursivo: n! = n * (n - 1)!
        return num * fact(num - 1)


def fact_n_numeros(num: int) -> None:
    """
    Calcula el factorial de todos los números entre 1 y num.
    :param num: int - Número entero positivo
    :return: None
    """
    for i in range(1, num + 1):
        # Llama a la función factorial para cada número y muestra el resultado en pantalla
        print(f"El factorial de {i} es: {fact(i)}")


# Se le pide al usuario un número entero positivo y se calcula el factorial de todos los números entre 1 y ese número.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# fact_n_numeros(int(input("Indique un número para calcular el factorial -> ")))


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.


def fibo(pos: int) -> int:
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada.
    :param pos: int - Posición en la serie de Fibonacci
    :return: int - Valor en la posición indicada
    """
    if pos == 0:
        # Caso base 1: el primer número de la serie es 0
        return 0
    elif pos == 1:
        # Caso base 2: el segundo número de la serie es 1
        return 1
    else:
        # Caso recursivo: F(n) = F(n-1) + F(n-2)
        return fibo(pos - 1) + fibo(pos - 2)


def serie_fibo(pos: int) -> None:
    """
    Muestra la serie de Fibonacci hasta la posición indicada.
    :param pos: int - Posición en la serie de Fibonacci
    :return: None
    """
    print("Serie de Fibonacci -> ", end="")
    for i in range(pos + 1):
        # Llama a la función Fibonacci para cada posición y muestra el resultado en pantalla
        # Se utiliza end=" " para que los números se muestren en la misma línea
        print(fibo(i), end=" ")


# Se le pide al usuario una posición y se muestra la serie de Fibonacci hasta esa posición.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# serie_fibo(int(input("Indique una posición para calcular la serie -> ")))


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.


def pot(base: int, exp: int) -> int:
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.
    :param base: int - Base de la potencia
    :param exp: int - Exponente de la potencia
    :return: int - Resultado de la potencia
    """
    if exp == 0:
        # Caso base: cualquier número elevado a la potencia 0 es 1
        return 1
    else:
        # Caso recursivo: n^m = n * n^(m-1)
        return base * pot(base, exp - 1)

    # Forma alternativa: Operador ternario 3️⃣
    # return 1 if exp == 0 else base * pot(base, exp - 1)


# Se le pide al usuario una base y un exponente, y se calcula la potencia.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# base = int(input("Indique la base -> "))
# exp = int(input("Indique el exponente -> "))
# print(f"La potencia de {base} elevado a {exp} es -> {pot(base, exp)}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.


def decimal_a_binario(num: int) -> str:
    """
    Convierte un número decimal a su representación binaria mediante divisiones recursivas.
    :param num: int - Número decimal a convertir
    :return: str - Representación binaria del número
    """
    if num == 0:
        # Caso base 0: si el número es 0, su representación binaria es "0"
        return "0"
    elif num == 1:
        # Caso base 1: si el número es 1, su representación binaria es "1"
        return "1"
    else:
        # Caso recursivo: divide el número por 2 y concatena el resultado de la llamada recursiva
        return decimal_a_binario(num // 2) + str(num % 2)


# Se le pide al usuario un número entero positivo y se muestra su representación binaria.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# print(decimal_a_binario(int(input("Indique un número para convertir a binario -> "))))


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.

# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra: str) -> bool:
    """
    Verifica si una palabra es un palíndromo de forma recursiva.
    :param palabra: str - Cadena de texto a verificar
    :return: bool - True si es un palíndromo, False en caso contrario
    """
    if len(palabra) <= 1:
        # Caso base: una palabra de longitud 0 o 1 es un palíndromo
        return True
    else:
        # Compara el primer y último carácter de la palabra
        if palabra[0] == palabra[-1]:
            # Caso recursivo: llama a la función recursivamente con la palabra sin los extremos
            return es_palindromo(palabra[1:-1])
        else:
            # Si los extremos no son iguales, no es un palíndromo
            return False


# Se le pide al usuario una palabra y se verifica si es un palíndromo.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# print(
#     es_palindromo(
#         input("Escriba una palabra para verificar si es palíndromo -> ").lower()
#     )
# )


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

# Ejemplos:
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4)
# suma_digitos(9)      → 9
# suma_digitos(305)    → 8   (3 + 0 + 5)


def suma_digitos(n: int) -> int:
    """
    Calcula la suma de los dígitos de un número entero positivo de forma recursiva.
    :param n: int - Número entero positivo
    :return: int - Suma de los dígitos del número
    """
    if n == 0:
        # Caso base: si el número es 0, la suma es 0
        return 0
    else:
        # Caso recursivo: suma el último dígito (n % 10) y llama a la función
        # recursivamente con el número sin el último dígito (n // 10)
        return n % 10 + suma_digitos(n // 10)


# Se le pide al usuario un número entero positivo y se calcula la suma de sus dígitos.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# print(
#     suma_digitos(
#         int(input("Indique un número para calcular la suma de sus dígitos -> "))
#     )
# )


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

# Ejemplos:
# contar_bloques(1)   → 1         (1)
# contar_bloques(2)   → 3         (2 + 1)
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)


def contar_bloques(n: int) -> int:
    """
    Calcula el total de bloques necesarios para construir una pirámide.
    :param n: int - Número de bloques en el nivel más bajo
    :return: int - Total de bloques necesarios
    """
    # Operador ternario: si n es 1, retorna 1; de lo contrario, suma n y llama a la función
    # recursivamente con n - 1
    return n if n == 1 else n + contar_bloques(n - 1)


# Se le pide al usuario un número entero positivo y se calcula el total de bloques necesarios.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# print(
#     contar_bloques(int(input("Indique el número de bloques en el nivel más bajo -> ")))
# )


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

# Ejemplos:
# contar_digito(12233421, 2)   → 3
# contar_digito(5555, 5)       → 4
# contar_digito(123456, 7)     → 0


def contar_digito(numero: int, digito: int) -> int:
    """
    Cuenta cuántas veces aparece un dígito en un número entero positivo de forma recursiva.
    :param numero: int - Número entero positivo
    :param digito: int - Dígito a contar (entre 0 y 9)
    :return: int - Cantidad de veces que aparece el dígito en el número
    """
    if numero == 0:
        # Caso base: si el número es 0, no hay más dígitos para contar
        return 0
    else:
        # Caso recursivo: compara el último dígito del número con el dígito a contar
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


# Se le pide al usuario un número entero positivo y un dígito, y se cuenta cuántas veces aparece el dígito en el número.
#! DESCOMENTAR ABAJO PARA PROBAR ⬇️
# print(
#     contar_digito(
#         int(input("Indique un número entero positivo -> ")),
#         int(input("Indique un dígito (0-9) -> ")),
#     )
# )

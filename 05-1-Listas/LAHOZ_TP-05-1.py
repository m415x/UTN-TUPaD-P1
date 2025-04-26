# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

# Crea una lista con los múltiplos de 4 del 1 al 100
multiplos_de_cuatro = list(range(4, 101, 4))
# Imprime la lista resultante por pantalla
print(multiplos_de_cuatro)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

# Crea una lista con cinco elementos (hobbies)
lista_hobbies = ["pedalear", "leer", "correr", "programar", "cocinar"]
# Imprime el penúltimo elemento de la lista utilizando el índice -2
print(lista_hobbies[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

# Crea una lista vacía
lista_vacia = []
# Agrega tres palabras a la lista utilizando append
lista_vacia.append("teclado")
lista_vacia.append("mouse")
lista_vacia.append("monitor")
# Imprime la lista resultante por pantalla
print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!

# Crea una lista con cuatro animales
animales = ["perro", "gato", "conejo", "pez"]
# Reemplaza el segundo valor (índice 1) por "loro"
animales[1] = "loro"
# Reemplaza el último valor (índice -1) por "oso"
animales[-1] = "oso"
# Imprime la lista resultante por pantalla
print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# El programa crea una lista de números desordenados
numeros = [8, 15, 3, 22, 7]
# Elimina el número máximo utilizando la función max()
numeros.remove(max(numeros))
# Imprime la lista resultante
print(numeros)

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

# Crea una lista con números del 10 al 30, haciendo saltos de 5 en 5
multiplos_de_cinco = list(range(10, 31, 5))
# Imprime los dos primeros elementos de la lista utilizando slicing
print(multiplos_de_cinco[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

# Crea una lista con cuatro autos
autos = ["sedan", "polo", "suran", "gol"]
# Reemplaza los valores centrales (índices 1 y 2) por "vento" y "passat"
autos[1] = "vento"
autos[2] = "passat"
# Imprime la lista resultante por pantalla
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

# Crea una lista vacía llamada "dobles"
dobles = []
# Agrega el doble de 5, 10 y 15 utilizando append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
# Imprime la lista resultante por pantalla
print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# Crea una lista de compras con productos comprados por diferentes clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# Agrega "jugo" a la lista del tercer cliente utilizando append
compras[2].append("jugo")
# Reemplaza "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"
# Elimina "pan" de la lista del primer cliente
compras[0].remove("pan")
# Imprime la lista resultante por pantalla
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

# Crea una lista anidada con los elementos especificados en la ubicación especificada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
# Imprime la lista resultante por pantalla
print(lista_anidada)

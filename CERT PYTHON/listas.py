""" module listas """

""" Listas: es una estructura de datos lineal y dinámica que se puede considerar como una variable pero que se puede almacenar más de un único valor """


numeros = [1, 2, 3]
print(numeros)
print(type(numeros))

nombres = ["Ulises", "Gio", "Hugo"]
print(nombres)

valores = [25, 2.999, 2.3, 1 + 2j, "a", "Uliches", True]
print(valores)
print(type(valores))

lista_anidada = [100, 90, 80, [1, 2, 2]]
print(lista_anidada)

unir_listas = numeros + nombres
print(unir_listas)

decimales = [1.2, 4.5, 6.3, 7, 8, 9]
print(decimales)
print(len(decimales))
print(decimales[2])
# 1 indica la posicion del indice y el 2 cuantos elementos a partir de ahí
print(decimales[1:3])

print(decimales[0:2])
print(decimales[-1])
print(decimales[-3])
""" print(decimales[-4]) hay error"""
print(decimales[-2:-1])
print(decimales[-3:-1])
print(decimales[0:3:2])  # el 2 es un salto de dos en dos
print(decimales[::-1])

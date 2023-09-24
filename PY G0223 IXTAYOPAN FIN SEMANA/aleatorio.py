""" module aleatorio """

import random

""" numero_aleatorio = random.uniform(1, 10)
print(numero_aleatorio)
 """

lista_vacia = []
for elemento in range(5):
    lista_vacia.append(random.randint(1, 10))

lista_llena = lista_vacia
print(lista_llena)

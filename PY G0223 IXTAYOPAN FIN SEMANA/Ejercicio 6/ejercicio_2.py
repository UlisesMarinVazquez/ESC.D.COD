""""" module ejercicio_2 """


""" def no_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def imprimir_primos(cantidad):
    primos_encontrados = 0
    numero = 2
    while primos_encontrados < cantidad:
        if no_primo(numero):
            print(numero, end=' ')
            primos_encontrados += 1
        numero += 1


try:
    cantidad = int(
        input("Ingrese la cantidad de números primos que desea imprimir: "))
    if cantidad <= 0:
        print("Por favor, ingrese un número positivo mayor que cero.")
    else:
        imprimir_primos(cantidad)
except ValueError:
    print("Ingrese un número válido.") """


primos_encontrados = 0
numero = 2

try:
    cantidad = int(
        input("Ingrese la cantidad de números primos que desea imprimir: "))
    if cantidad <= 0:
        print("Por favor, ingrese un número positivo mayor que cero.")
    else:
        while primos_encontrados < cantidad:
            es_primo = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(numero, end=' ')
                primos_encontrados += 1
            numero += 1
except ValueError:
    print("Ingrese un número válido.")

 
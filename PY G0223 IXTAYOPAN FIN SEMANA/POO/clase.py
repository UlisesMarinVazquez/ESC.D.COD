
"""module clase"""


class Celular:
    marca = "Nokia"
    modelo = "Plus"
    color = "Negro"

# Instanciar un obj a partir de la clase Celular


celular_1 = Celular()
print(celular_1)

# Mostrar atributos
print(celular_1.marca)
print(celular_1.modelo)
print(celular_1.color)

# Vamos a crear objetos iguales

celular_2 = Celular()
celular_3 = Celular()
celular_4 = Celular()

""" class Celurares:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color """

def 
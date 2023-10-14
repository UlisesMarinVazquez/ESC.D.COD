class Celulares:
    def __init__(self, marca="Apple", modelo="iphone 15", color="Titanio"):
        self.marca = marca
        self.modelo = modelo
        self.color = color


celular1 = Celulares("Xiaomi", "SG10", "Rojo")
celular2 = Celulares()

print(celular1.marca, celular1.modelo, celular1.color)
print(celular2.marca, celular2.modelo, celular2.color)

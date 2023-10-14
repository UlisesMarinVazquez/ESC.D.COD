""""module ejercicio copy"""


class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
# setter y getter

# crear un getter

    def mostrar(self):
        return f"El nombre de la persona: {self.nombre} su edad es {self.edad} y DNI es {self.dni}"
    # setter

    def esMayorDeEdad(self):
        if self.edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad.")


Persona_1 = Persona("Juan", 25, "ABD213")
print(Persona_1.mostrar())
print(Persona_1.esMayorDeEdad())

Persona_2 = Persona("ANA", 30, "BSCX2")
print(Persona_2.mostrar())


# herencia capacidad que tiene la super clase de heredar los atributos y metodos a una subclase

""""module ejercicio"""


class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

     # self.__nombre = nombre
       # self.__edad = edad
        # self.__dni = dni


# print(persona_1._Persona__nombre, persona_1._Pesona__edad, Persona_1._Persona__dni)

# setter y getter

# crear un setter


def mostrar(self):
    return f"El nombre de la persona es: {self.nombre} su edad es {self.edad} y su DNI es {self.dni}"


Persona_1 = Persona("Juan", 25, "ABD213")
print(Persona_1.mostrar())
Persona_2 = Persona("ANA", 30, "BSCX2")
print(persona_2.mostrar())

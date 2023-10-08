
"""module ejercicio_1"""


""" class Persona:
    nombre = ""
    edad = 0
    dni = ""


persona_1 = Persona()
print(persona_1)
 """


class Persona:  # Metodo de inicializacion # Metodo constructor
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Setter y Getter para nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    # Setter y Getter para edad con validación
    def setEdad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser negativa")

    def getEdad(self):
        return self.edad

    # Setter y Getter para DNI
    def setDni(self, dni):
        self.dni = dni

    def getDni(self):
        return self.dni

    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    # Método para comprobar si la persona es mayor de edad
    def esMayorDeEdad(self):
        return self.edad >= 18


# Ejemplo de uso:
persona1 = Persona()
persona1.setNombre("Juan")
persona1.setEdad(25)
persona1.setDni("12345678A")

persona1.mostrar()
print("¿Es mayor de edad?", persona1.esMayorDeEdad())

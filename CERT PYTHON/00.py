""" from datetime import datetime, date

class CalculadoraDiasVida:
    def __init__(self, birth_year, birth_month, birth_day):
        self.birth_date = date(birth_year, birth_month, birth_day)
        self.current_date = date.today()

    def calcular_dias_vida(self):
        days_alive = (self.current_date - self.birth_date).days
        return days_alive

    def imprimir_dias_vida(self):
        days_alive = self.calcular_dias_vida()
        print(f"Has vivido {days_alive} días hasta el día de hoy.")

# Solicitar la fecha de nacimiento al usuario
year = int(input("Ingresa tu año de nacimiento: "))
month = int(input("Ingresa tu mes de nacimiento: "))
day = int(input("Ingresa tu día de nacimiento: "))

# Crear una instancia de la clase CalculadoraDiasVida
calculadora = CalculadoraDiasVida(year, month, day)

# Calcular y mostrar los días de vida
calculadora.imprimir_dias_vida() """



# Programa de preguntas y respuestas con booleanos en Python

# Función para hacer una pregunta y obtener la respuesta del usuario
def hacer_pregunta(pregunta):
    respuesta = input(pregunta + " (responde sí o no): ").strip().lower()
    return respuesta == "sí"

# Preguntas al usuario y almacenamiento de respuestas como booleanos
respuesta1 = hacer_pregunta("¿Te gusta el chocolate?")
respuesta2 = hacer_pregunta("¿Has viajado al extranjero?")
respuesta3 = hacer_pregunta("¿Te gustan los deportes?")
respuesta4 = hacer_pregunta("¿Has leído un libro este mes?")

# Imprimir las respuestas
print("Respuesta 1:", respuesta1)
print("Respuesta 2:", respuesta2)
print("Respuesta 3:", respuesta3)
print("Respuesta 4:", respuesta4)

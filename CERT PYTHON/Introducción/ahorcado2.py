


class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra.lower()
        self.intentos_restantes = 6
        self.letras_adivinadas = []

    def mostrar_palabra(self):
        palabra_mostrada = ""
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"
        return palabra_mostrada

    def adivinar_letra(self, letra):
        if letra in self.letras_adivinadas:
            return "Ya has adivinado esta letra antes."
        
        self.letras_adivinadas.append(letra)
        
        if letra in self.palabra:
            if self.mostrar_palabra() == self.palabra:
                return "¡Has adivinado la palabra! ¡Ganaste!"
            else:
                return "¡Buena adivinanza! Palabra actual: " + self.mostrar_palabra()
        else:
            self.intentos_restantes -= 1
            if self.intentos_restantes == 0:
                return "¡Agotaste tus intentos! La palabra era: " + self.palabra
            else:
                return "Letra incorrecta. Intentos restantes: " + str(self.intentos_restantes)

    def dibujar_ahorcado(self):
        dibujo = [
            "   _____",
            "  |     |",
            "  |     " + ("O" if self.intentos_restantes < 6 else ""),
            "  |    " + ("/" if self.intentos_restantes < 4 else " ") + ("|" if self.intentos_restantes < 5 else ""),
            "  |    " + ("/" if self.intentos_restantes < 3 else "") + (" \\" if self.intentos_restantes < 2 else ""),
            "  |",
            "__|__"
        ]
        return "\n".join(dibujo)


# Función para comenzar el juego
def jugar():
    palabra_secreta = input("Ingresa la palabra secreta: ")
    juego = Ahorcado(palabra_secreta)

    print("¡Bienvenido al juego de ahorcado!")
    print("Palabra actual: " + juego.mostrar_palabra())

    while juego.intentos_restantes > 0:
        letra = input("Adivina una letra: ")
        resultado = juego.adivinar_letra(letra)
        print(resultado)
        print(juego.dibujar_ahorcado())
        if "ganaste" in resultado or "agotaste" in resultado:
            break

    print("Fin del juego.")

# Iniciar el juego
jugar()

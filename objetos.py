class Humano:
    def __init__(self,edad):
        self.edad = edad
        print("Soy un nuevo objeto")

    def hablar(self, mensaje):
        print(mensaje)


Pedro = Humano(26)

Raul = Humano(21)

print ("Soy Pedro y tengo ", Pedro.edad)
print("Soy Raul y tengo ", Raul.edad)
Pedro.hablar("Hola")

Raul.hablar("Hola, Pedro")

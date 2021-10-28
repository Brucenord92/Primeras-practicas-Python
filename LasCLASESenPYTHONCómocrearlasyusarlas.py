class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "se ha arrancado")

    def parar(self):
        self.arrancado = False
        print("El", self.marca, self.modelo, "se ha parado")   

Dbs = Coche("Aston Martin", "Dbs")
print(type(Dbs))

print(Dbs.marca, Dbs.modelo)


Dbs.arrancar()

print(Dbs.arrancado)


Dbs.parar()

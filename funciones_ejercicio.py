def Puntuación(clase):
    return sum(clase) / len(clase)


clase = [7, 8, 9]
media = Puntuación(clase)
print("La puntuación media de la clase es: ", media)
clase = [5, 8, 9, 6]
media = Puntuación(clase)
print("La puntuación media de la clase es: ", media)


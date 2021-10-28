print("Sistema para calcular promedio de un alumno")

nombre = input("¿Cual es tu nombre?: ")

Matematicas = int(input("¿Cual es tu calificacion en matematicas?: "))
Historia = int(input("¿Cual es tu calificacion en historia?: "))
Quimica = int(input("¿Cual es tu calificacion en quimica?: "))

promedio = (Matematicas + Historia + Quimica) / 3
promedio = int(promedio)

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
else:
    print("Lo sentimos has reprobado el curso ", "con una nota de:",  promedio)

print("Fin.")




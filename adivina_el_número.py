import random
intentosRealizados = 0
print("Hola ¿Cómo te llamas?")
miNombre = input()

número = random.randint(1, 20)

print("Bueno, " + miNombre + " Estoy pensando un número entre el 1 y 20. ")

while intentosRealizados < 6:
    print("Intenta adivinar")
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print("Tu estimación es muy baja")

    if estimación > número:
        print("Tu estimación es muy alta")

    if estimación == número:
        break
if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print("Buen trabajo " + miNombre + " haz adivinado mi número en " + intentosRealizados + " intentos")

    if estimación != número:
        print("Pues no. El número que estaba pensando era ", número)
        

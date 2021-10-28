print("**************************************************************************")
print("Programa para determinar el numero mas grande seleccionado por el usuario.")
print("**************************************************************************")


numero_uno = int(input("Introduce el primer numero: "))

numero_dos = int(input("Introduce el segundo numero: "))

numero_tres = int(input("Introduce el tercer numero: "))


if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El numero", numero_uno, "es el mas grande de los tres.")

elif numero_dos > numero_uno and numero_dos > numero_tres:
    print("El numero", numero_dos, "es el mas grande de los tres.")

elif numero_tres > numero_uno and numero_tres > numero_dos:
    print("El numero", numero_tres, "es el mas grande de los tres.")

else:
    ("Error intente de nuevo, por favor.")
    

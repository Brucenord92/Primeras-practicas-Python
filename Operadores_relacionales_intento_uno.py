print("Introduce dos numeros a comparar: ")

print(input(" \n Introduce el primer numero: \n "))
print(input(" \n Introduce el segundo numero: \n "))

primer_numero = int(input())
segundo_numero = int(input())

if primer_numero <= segundo_numero:
    print("Menor o igual.")
elif primer_numero >= segundo_numero:
    print("Mayor o igual.")
elif primer_numero == segundo_numero:
    print("Igual.")
else:
    print("Opcion invalida.")



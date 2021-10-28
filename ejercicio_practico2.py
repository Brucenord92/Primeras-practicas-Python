print("***************************************************")
print("Programa que determina si un numero es par o impar ")
print("***************************************************")

numero = int(input("Por favor introduce un numero entero: "))

if numero % 2 == 0:
    print(numero, "tu numero es par.")
    
elif numero % 2 != 0:
    print(numero, "tu numero es impar")

else:
    print("Este programa solo acepta numeros enteros para funcionar.")
    

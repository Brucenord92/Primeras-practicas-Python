print("************")
print("Calculadora")
print("************")


print("Menu de opciones \n")

print("1.Suma")
print("2. Resta")
print("3. multiplicacion")
print("4. division")
print("5. division entera")
print("6. Exponente")
print("7. Resto")

numero = int(input("Introduce la opcion deseada:" ))

if numero == 1:
    print("Elegiste suma \n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es:", numero)

elif numero == 2:
    print("Elegiste resta \n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es:", numero)
    

elif numero == 3:
    print("Elegiste multiplicacion.")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicacion es:", numero)
    

elif numero == 4:
    print("Elegiste division.")
    numero = int(input("Introduce el primer numero: "))
    numero /= int(input("Introduce el segundo numero: "))
    print("El resultado de la division es:", round(numero, 2))

elif numero == 5:
    print("Elegiste division entera.")
    numero = int(input("Introduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado de la division entera es:", numero)

elif numero == 6:
    print("Elegiste exponente.")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado del exponente es:", numero)

elif numero == 7:
    print("Elegiste modulo o resto.")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El resultado del modulo es:", numero)
    

else:
    print("Error. intente de nuevo, por favor")


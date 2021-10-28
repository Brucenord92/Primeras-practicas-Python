print("==================================")
print("Sistema de vacaciones para Rappi")
print("==================================")

nombre = input("¿Cual es tu nombre? " )

clave = int(input("¿Cual es tu clave?" ))

años = float(input("¿Cuantos años llevas trabajando? " ))


if clave == 1 and años == 1:
    print(nombre,"tu clave es", clave, "Tienes derecho a seis dias de vacaciones. " )

elif clave == 1 and años <= 6:
    print(nombre,"tu clave es", clave, "Tienes derecho a catorce dias de vacaciones. " )

elif clave == 1 and años >= 7:
    print(nombre,"tu clave es", clave, "Tienes derecho a veinte dias de vacaciones. " )


elif clave == 2 and años == 1:
    print(nombre,"tu clave es", clave, "Tienes derecho a siete dias de vacaciones. " )

elif clave == 2 and años <= 6:
    print(nombre,"tu clave es", clave, "Tienes derecho a quince dias de vacaciones. " )
    
elif clave == 2 and años >= 7:
    print(nombre,"tu clave es", clave, "Tienes derecho a veintidos dias de vacaciones. " )

elif clave == 3 and años == 1:
    print(nombre,"tu clave es", clave, "Tienes derecho a diez dias de vacaciones. " )
 
elif clave == 3 and años <= 6:
    print(nombre,"tu clave es", clave, "Tienes derecho a veinte dias de vacaciones. " )

elif clave == 3 and años >= 7:
    print(nombre,"tu clave es", clave, "Tienes derecho a treinta dias de vacaciones. " )

else:
    print("No tienes derecho a vacaciones. ")
        


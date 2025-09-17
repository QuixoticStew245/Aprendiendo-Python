# Crea un programa que pida la edad y si tiene credencial de estudiante (sí/no).
#Si tiene menos de 18 o es estudiante, imprime "Tienes descuento".
#En otro caso, imprime "No tienes descuento".

edad = int(input("Ingrese su edad: "))

if edad < 18 and edad >= 5:
    credencial = input("¿Tiene credencial de estudiante? (s/n): ").lower()
    if credencial == 's':
        print("Tienes descuento")
    elif credencial == 'n':
        print("No tienes descuento")
    else:
        print("Respuesta no válida")

elif edad >= 18 and edad < 100:
    print("No tienes descuento")

else:
    print("Edad no válida para descuento")
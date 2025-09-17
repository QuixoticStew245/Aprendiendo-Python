#Convierte un número decimal introducido por el usuario a entero.

numero = float(input("Ingrese un número decimal: "))
entero = int(numero)
numero = round(numero)
print("Número redondeado:", numero)
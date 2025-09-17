nombre = ""

# Bucle infinito que se rompe con "break"
while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre != "":# Si el usuario escribe algo (no vacío)
        print("Hola " + nombre)
        break# Rompe el bucle y continúa con el resto del programa


telefono = "123-456-789"

# Recorremos cada caracter de la cadena "telefono"
for i in telefono:
    if i == "-":# Si el caracter es un guión
        continue# Saltamos esa iteración (no se ejecuta el print)
    print(i, end="")# Imprime los números uno tras otro sin salto de línea

print()# salto de línea para separar la salida

# Recorremos del 1 al 20
for i in range(1, 21):
    if i == 13:
        pass# "pass" no hace nada, simplemente deja el bloque vacío
    else:
        print(i)

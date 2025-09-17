# Pedimos la temperatura al usuario y la convertimos a número entero
temperatura = int(input("Cual es la temperatura a fuera? "))

# Primera versión usando "and" y "or"
if temperatura >= 0 and temperatura <= 30:
    # Si la temperatura está entre 0 y 30 (incluyendo ambos)
    print("La temperatura esta bien hoy :D")
elif temperatura < 0 or temperatura > 30:
    # Si la temperatura es menor que 0 o mayor que 30
    print("La temperatura esta mal hoy :(")


# Pedimos otra vez la temperatura para la segunda versión
temperatura = int(input("Cual es la temperatura a fuera? "))

# Segunda versión usando "not"
if not(temperatura >= 0 and temperatura <= 30):
    # "not" invierte la condición
    # Esto significa: si la temperatura NO está entre 0 y 30
    print("La temperatura esta mal hoy :(")
elif not(temperatura < 0 or temperatura > 30):
    # Aquí pasa lo contrario:
    # si la temperatura NO es menor que 0 ni mayor que 30
    # significa que está dentro del rango de 0 a 30
    print("La temperatura esta bien hoy :D")

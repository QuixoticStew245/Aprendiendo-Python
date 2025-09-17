# Crea una lista de números y calcula la suma total sin usar la función sum().
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma_total = 0
for num in numero:
    suma_total += num
print("La suma total es:", suma_total)
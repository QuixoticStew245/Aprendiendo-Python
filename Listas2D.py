# Lista de bebidas
bebidas = ["cafe", "soda", "te"]

# Lista de platos principales
cena = ["pizza", "hamburguesa", "hot dog"]

# Lista de postres
postres = ["pastel", "helado"]

# Creamos una lista que contiene las otras listas
comida = [bebidas, cena, postres]
# comida = [
#   ["cafe", "soda", "te"],
#   ["pizza", "hamburguesa", "hot dog"],
#   ["pastel", "helado"]
# ]

# Accedemos al índice 2 de 'comida' (la tercera lista → postres)
# Y dentro de esa lista, accedemos al índice 1 (segundo elemento → "helado")
print(comida[2][1])

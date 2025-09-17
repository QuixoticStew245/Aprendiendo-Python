# Pedimos al usuario cuántas filas quiere
fila = int(input("Cuantas filas? "))

# Pedimos cuántas columnas quiere
columna = int(input("Cuantas columnas? "))

# Pedimos el símbolo con el que se construirá el rectángulo
simbolo = input("Ingresa un simbolo: ")

# Bucle externo: recorre cada fila
for i in range(fila):
    # Bucle interno: recorre cada columna dentro de una fila
    for j in range(columna):
        # Imprime el símbolo sin salto de línea (end="")
        print(simbolo, end="")
    # Cuando termina una fila, hacemos un salto de línea
    print()

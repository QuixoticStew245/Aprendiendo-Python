#Representa una matriz 3x3 con números del 1 al 9 e imprime los elementos en forma de cuadrado.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()
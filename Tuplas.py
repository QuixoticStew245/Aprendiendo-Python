# Definimos una tupla (inmutable, no se puede modificar después de creada)
estudiantes = ('Alex', 22, 'M', 'Anto', 22, 'F')

# count() devuelve cuántas veces aparece el valor dentro de la tupla
print(estudiantes.count(22))   #Resultado: 2 (porque hay dos veces el número 22)

# index() devuelve el índice (posición) de la primera vez que aparece el valor
print(estudiantes.index('M'))  #Resultado: 2 (porque 'M' está en la posición 2)

# Recorremos todos los elementos de la tupla con un bucle for
for x in estudiantes:
    print(x)

# Verificamos si 'Alex' existe dentro de la tupla
if 'Alex' in estudiantes:
    print("Alex esta aqui")

#Una tupla (tuple) es inmutable, 
# a diferencia de una lista, no puedes hacer append(), remove(), etc.
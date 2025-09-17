# Creamos una lista con diferentes tipos de datos (strings, int, float, bool)
comidas = ['Pizza', 'Hamburguesa', 'Hot dog', 'Espaguetis', 'Pudding', 2, 0.5, False]

# Cambiamos el primer elemento de la lista
comidas[0] = 'Helado'     
# ['Helado', 'Hamburguesa', 'Hot dog', 'Espaguetis', 'Pudding', 2, 0.5, False]

# Agregamos un nuevo elemento al final
comidas.append('Sushi')   
# ['Helado', 'Hamburguesa', 'Hot dog', 'Espaguetis', 'Pudding', 2, 0.5, False, 'Sushi']

# Eliminamos el primer elemento con valor 'Hamburguesa'
comidas.remove('Hamburguesa')
# ['Helado', 'Hot dog', 'Espaguetis', 'Pudding', 2, 0.5, False, 'Sushi']

# Eliminamos el último elemento de la lista
comidas.pop()
# ['Helado', 'Hot dog', 'Espaguetis', 'Pudding', 2, 0.5, False]

# Insertamos 'Pastel' en el índice 0 (al principio de la lista)
comidas.insert(0, 'Pastel')
# ['Pastel', 'Helado', 'Hot dog', 'Espaguetis', 'Pudding', 2, 0.5, False]

# Ordenamos la lista (dará error porque hay mezcla de strings, int, float, bool → no son comparables en Python 3)
# comidas.sort()

# Vaciamos la lista completamente → si descomentas esta línea, la lista quedará en []
# comidas.clear()

# Como la lista ya no está vacía (porque el clear está comentado), imprime todos los elementos
for x in comidas:
    print(x)

# Imprime el primer elemento de la lista (sería "Pastel")
# ⚠️ Ojo: si activas comidas.clear(), aquí dará IndexError porque ya no hay elementos
print(comidas[0])

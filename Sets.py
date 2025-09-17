# Creamos un set llamado 'utensilios' con 3 elementos
utensilios = {"tenedor", "cuchara", "cuchillo"}

# Creamos otro set llamado 'platos' con 4 elementos
platos = {"plato", "bol", "taza", "cuchara"}

# ---------------------
# Métodos útiles de sets
# ---------------------

# .add(elemento) -> agrega un elemento al set
# utensilios.add("plato")  # agregaría "plato" a utensilios

# .remove(elemento) -> elimina un elemento específico (da error si no existe)
# utensilios.remove("cuchara")  # eliminaría "cuchara" del set

# .discard(elemento) -> elimina un elemento específico sin error si no existe
# utensilios.discard("cuchara")

# .pop() -> elimina un elemento aleatorio del set
# utensilios.pop()

# .clear() -> elimina todos los elementos del set
# utensilios.clear()

# .update(otro_set) -> agrega todos los elementos de otro set
# utensilios.update(platos)

# ---------------------
# Operaciones entre sets
# ---------------------

# .difference(otro_set) -> elementos que están en el primer set pero NO en el segundo
# print(utensilios.difference(platos))  # resultado: {"tenedor", "cuchillo"}

# .intersection(otro_set) -> elementos que están en ambos sets
print(utensilios.intersection(platos))  # resultado: {'cuchara'}

# ---------------------
# Recorrer un set
# ---------------------

# Un bucle for puede recorrer todos los elementos de un set
# for x in utensilios:
#     print(x)  # imprime cada elemento (el orden puede variar)

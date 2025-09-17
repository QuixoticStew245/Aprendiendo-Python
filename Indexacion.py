# Definimos una variable con un nombre completo
nombre = 'derek Ortiz!'

# ---------------------
# Comprobar si la primera letra está en minúscula
# ---------------------
# .islower() verifica si un carácter está en minúscula
# if nombre[0].islower():
#     nombre = nombre.capitalize()  # .capitalize() pone la primera letra en mayúscula y las demás en minúscula
# print(nombre)

# ---------------------
# Extraer y modificar partes del nombre
# ---------------------

# [:5] -> toma los primeros 5 caracteres (del índice 0 al 4)
# .upper() -> convierte todo a mayúsculas
primer_nombre = nombre[:5].upper()  # 'derek' -> 'DEREK'

# [6:] -> toma los caracteres desde el índice 6 hasta el final
# .lower() -> convierte todo a minúsculas
apellido = nombre[6:].lower()  # 'Ortiz!' -> 'ortiz!'

# [-1] -> accede al último carácter de la cadena
ultimo_caracter = nombre[-1]  # '!'

# ---------------------
# Mostrar los resultados
# ---------------------
print(primer_nombre)      # Imprime: DEREK
print(apellido)           # Imprime: ortiz!
print(ultimo_caracter)    # Imprime: !

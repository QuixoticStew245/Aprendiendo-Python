# Creamos un diccionario llamado 'capitales'
# Un diccionario (dict) almacena pares clave:valor
# La clave es única y sirve para acceder a su valor
capitales = {
    'EEUU': 'Washington, D.C.',
    'Mexico': 'Ciudad de México',
    'España': 'Madrid',
    'Brasil': 'Brasilia',
    # Un valor puede ser una lista, no solo un string
    'Lenguajes de Programación': ['Python', 'Java', 'C++'],
    'Años' : [2020, 2021, 2022, 2023]
}

# .update() -> agrega o actualiza pares clave:valor en el diccionario
capitales.update({'Argentina': 'Buenos Aires'})

# .pop(clave) -> elimina un par clave:valor y devuelve el valor eliminado
capitales.pop('EEUU')  # elimina la clave 'EEUU'

# .clear() -> elimina todos los elementos del diccionario
# capitales.clear()  # comentado para no vaciar el diccionario

# ---------------------
# Métodos útiles para acceder a datos
# ---------------------

# .get(clave) -> obtiene el valor de una clave (si no existe, devuelve None)
# print(capitales.get('España'))  # Madrid

# .keys() -> devuelve todas las claves
# print(capitales.keys())  # dict_keys(['Mexico', 'España', 'Brasil', ...])

# .values() -> devuelve todos los valores
# print(capitales.values())  # dict_values(['Ciudad de México', 'Madrid', ...])

# .items() -> devuelve pares clave:valor
# print(capitales.items())  # dict_items([('Mexico', 'Ciudad de México'), ...])

# ---------------------
# Recorrer el diccionario
# ---------------------

# for key, value in capitales.items() -> recorre todos los pares clave:valor
for key, value in capitales.items():
    # Imprime de manera legible
    print(f'La capital de {key} es {value}')

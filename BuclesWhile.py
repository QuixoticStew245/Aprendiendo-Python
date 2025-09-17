# Creamos una variable vacía al inicio
nombre = ""

# Mientras 'nombre' esté vacío (""), o su longitud sea 0
# se repetirá el bucle pidiendo un nombre
while not nombre or len(nombre) == 0:
    nombre = input("Ingresa tu nombre: ")

# Cuando el bucle termina significa que ya tenemos un nombre válido
print("Hola " + nombre)

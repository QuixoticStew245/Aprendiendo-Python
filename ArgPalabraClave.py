# Definimos una función llamada "saludo" que recibe 3 parámetros:
# - nombre: el primer nombre de la persona
# - apellido: el apellido de la persona
# - lenguaje: el lenguaje de programación que está aprendiendo
def saludo(nombre, apellido, lenguaje):
    # Usamos una f-string para mostrar un mensaje en pantalla.
    # Las llaves {} permiten insertar directamente el valor de las variables dentro del texto.
    print(f"Hola {nombre} {apellido}, estas aprendiendo {lenguaje}")

# Llamamos a la función "saludo".
# Aquí estamos pasando los valores de los parámetros de manera "nombrada":
# - lenguaje = "Python"
# - apellido = "Perez"
# - nombre = "Juan"
# El orden no importa porque estamos indicando explícitamente el nombre de cada parámetro.
saludo(lenguaje="Python", apellido="Perez", nombre="Juan") 

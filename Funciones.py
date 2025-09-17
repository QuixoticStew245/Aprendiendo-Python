# ---------------------
# Definimos una función llamada 'saludo'
# ---------------------
# Una función es un bloque de código que podemos reutilizar
# Podemos pasarle información (parámetros) y hacer algo con ella
def saludo(primer_nombre, apellido, edad):
    # Imprime un saludo usando los parámetros
    print("Hola " + primer_nombre + " " + apellido + "!")
    # Convierte la edad a cadena con str() para poder concatenarla
    print("Tienes " + str(edad) + " años.")
    # Mensaje adicional
    print("Espero que tengas un buen día.")

# ---------------------
# Solicitamos información al usuario
# ---------------------
nombre = input("¿Cuál es tu nombre? ")  # input() devuelve un string con lo que escribe el usuario

# ---------------------
# Llamamos a la función 'saludo'
# ---------------------
# Pasamos los valores que necesitamos: nombre ingresado, apellido fijo y edad fija
saludo(nombre, "Ortiz", 19)

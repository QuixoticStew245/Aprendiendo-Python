# La función recibe varios números, convierte los argumentos en lista,
# cambia el segundo valor a 0 y luego suma todos los elementos.

def suma(*args):                 # *args permite recibir cualquier cantidad de números como argumentos.
    suma = 0                     # Creamos una variable para acumular la suma.
    cosas = list(args)           # Convertimos la tupla args a una lista (porque las tuplas no se pueden modificar).
    cosas[1] = 0                 # Cambiamos el segundo valor de la lista (índice 1) a 0.
    for i in cosas:              # Recorremos cada número de la lista.
        suma += i                # Vamos sumando cada valor en la variable 'suma'.
    return suma                  # Devolvemos el resultado final.

# Al llamar la función con estos números:
print(suma(1, 5, 3, 2, 7, 1))    # Los argumentos son: (1, 5, 3, 2, 7, 1)

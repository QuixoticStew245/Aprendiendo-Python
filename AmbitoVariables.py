nombre = "Ortiz"  # Variable global: está definida fuera de cualquier función
                  # y se puede usar en todo el programa.

def mostrar_nombre():
    nombre = "Derek"  # Variable local: solo existe dentro de la función.
                      # Esta "tapa" temporalmente a la variable global dentro de la función.
    print(nombre)     # Muestra la variable local ("Derek").

mostrar_nombre()      # Llama a la función, imprime "Derek".
print(nombre)         # Aquí ya no estamos dentro de la función,
                      # por lo tanto se usa la variable global ("Ortiz").
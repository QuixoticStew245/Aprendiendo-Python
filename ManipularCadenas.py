nombre = "Derek Ortiz"

# [0:5] significa: toma desde el índice 0 hasta el 5 (sin incluir el 5)
primerNombre = nombre[0:5]

# [6:] significa: toma desde el índice 6 hasta el final
apellido = nombre[6:]

# [::3] significa: toma todo el texto, saltando de 3 en 3 caracteres
# Índices tomados: 0, 3, 6, 9 → Letras: D, e, O, i
nombreDos = nombre[::3]

# [::-1] significa: invierte el texto
nombreInvertido = nombre[::-1]

website = "http://www.google.com"

# slice(11, -4) significa: toma desde el índice 11 hasta 4 posiciones antes del final
# El índice 11 es la "g" de google, y -4 corta el ".com"
Slice = slice(11, -4)

print(primerNombre)     # Derek
print(apellido)         # Ortiz
print(nombreDos)        # DeOi
print(nombreInvertido)  # zitrO kereD
print(website[Slice])   # google

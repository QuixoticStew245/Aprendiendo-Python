# Pedimos al usuario que escriba su edad
edad = int(input("Cual es tu edad? "))

# Comenzamos a evaluar condiciones con if/elif/else

# Si la edad es exactamente 100
if edad == 100:
    print("Tienes un siglo de vida")

# Si no es 100 pero la edad es mayor o igual a 18
elif edad >= 18:
    print("Eres mayor de edad!")

# Si no se cumple ninguna de las anteriores (edad < 18)
else:
    print("Eres menor de edad :(")

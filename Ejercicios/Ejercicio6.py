# Ejercicio 6: Solicitar al usuario que ingrese una contraseña hasta que ingrese la correcta.
# La contraseña correcta es "python123".

while True:
    print("La contraseña es python123")
    contraseña = input("Introduce una contraseña: ")
    if contraseña == "python123":
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, inténtalo de nuevo")
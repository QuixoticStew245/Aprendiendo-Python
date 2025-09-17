# Ejercicio 7: Escribir una función que reciba un número como parámetro y devuelva su cuadrado.
    
def cuadrado():
    numero = int(input("Ingrese un número: "))
    resultado = numero ** 2
    print(f"El cuadrado de {numero} es {resultado}")

cuadrado()
'''
num = input("Ingrese un numero: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
'''
# Se agrupan las funciones porque cada una usa el resultado de la anterior:
# primero se pide el número con input(), luego se convierte a float,
# después se obtiene el valor absoluto con abs(), se redondea con round()
# y finalmente se muestra en pantalla con print().
print(round(abs(float(input("Ingrese un numero: ")))))
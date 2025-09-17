# Ejercicio 14: Simulación de cajero automático
while True:
    try:
        pin = int(input("Ingrese su PIN: "))
        if pin == 1234:
            print("PIN correcto. Acceso concedido.")
            break
        else:
            print("PIN incorrecto. Inténtelo de nuevo.")
    except ValueError:
        print(" Entrada inválida. Por favor, ingrese un número entero para el PIN.")

print("Consulte su saldo(c) o deposite fondos(d) retirando el dinero(r)")
opcion = input("Ingrese su opción: ")
while True:
    if opcion == "c":
        print("Su saldo es de $1000")
        break
    elif opcion == "d":
        deposito = float(input("Ingrese la cantidad a depositar: "))
        if deposito > 0:
            print(f"Ha depositado ${deposito}. Su nuevo saldo es de ${1000 + deposito}")
            break
        else:
            print("Cantidad inválida. Inténtelo de nuevo.")
    elif opcion == "r":
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if 0 < retiro <= 1000:
            print(f"Ha retirado ${retiro}. Su nuevo saldo es de ${1000 - retiro}")
            break
        else:
            print("Cantidad inválida o fondos insuficientes. Inténtelo de nuevo.")
    else:
        print("Opción inválida. Por favor, elija 'c', 'd' o 'r'.")
    opcion = input("Ingrese su opción: ")

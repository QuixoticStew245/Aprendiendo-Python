import time   # Importamos la librería time, que nos permite pausar la ejecución del programa

# Usamos un bucle for con range(10, 0, -1)
# range(inicio, fin, paso)
# → Empieza en 10
# → Termina en 0 (pero sin incluir el 0)
# → Va restando de 1 en 1 (paso -1)
for s in range(10, 0, -1):
    print(s)          # Mostramos el número actual
    time.sleep(1)     # Pausamos el programa 1 segundo antes de seguir

# Cuando termina el bucle mostramos el mensaje final
print("Feliz año nuevo!")

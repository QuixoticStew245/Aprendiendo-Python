
def vocales(texto):
    texto = texto.lower()
    for vocales in "aeiou":
        print(f"{vocales}={sum(1 for letra in texto if letra == vocales)}")

vocales(texto="Webos")
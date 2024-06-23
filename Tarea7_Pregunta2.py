palabras = []
print("Ingrese palabras. Para finalizar, presione Enter sin ingresar una palabra.")

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "":
        break
    palabras.append(palabra)

def contar_a(palabra):
    contador = 0
    for letra in palabra:
        if letra == 'A' or letra == 'a':
            contador += 1
    return contador

print("Cantidad de letras 'A' o 'a' en cada palabra:")
for palabra in palabras:
    contador_a = contar_a(palabra)
    print("La palabra '" + palabra + "' tiene " + str(contador_a) + " letras 'A' o 'a'.")

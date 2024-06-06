palabras=[]
while True:
    palabra=input("Ingrese una palabra (Enter para finalizar)")
    if palabra=="":
        break
    palabras.append(palabra)

if palabras:
    menor_palabra=palabras[0]
    for palabra in palabras:
        len(palabra) < len(menor_palabra)
        menor_palabra=palabra

print("La palabra con menor caracteres tiene:", len(menor_palabra), "caracter.")







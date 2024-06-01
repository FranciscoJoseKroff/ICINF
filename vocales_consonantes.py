lista=[]
vocales="aeiouAEIOU"

while True:
    palabra=input("Ingrese una palabra para la lista (Enter para finalizar)")
    if palabra=="":
        break
    lista.append(palabra)

    for palabra in lista:
            cont_vocales = 0
            cont_consonantes = 0
            for letra in palabra:
                if (letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z'):
                    if letra in vocales:
                        cont_vocales += 1
                    else:
                          cont_consonantes += 1
    print("Vocales: " + str(cont_vocales) + ", Consonantes: " + str(cont_consonantes))
                    



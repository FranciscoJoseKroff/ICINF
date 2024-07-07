def separar(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    pares.sort()
    impares.sort()
    
    return pares, impares

lista = [6, 1, 4, 7, 8, 3, 2, 5]
pares, impares = separar(lista)

print("Numeros pares:", pares)
print("Numeros impares:", impares)
def convierte_negativo(lista):
    for num in lista:
        num=-num
        return num

lista=[]
print("Ingrese 10 numeros")
for x in range(10):
    num=int(input())
    lista.append(num)
numeros_negativos=convierte_negativo(lista)
print(numeros_negativos)

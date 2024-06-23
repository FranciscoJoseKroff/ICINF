lista=[]
for i in range(10):
    numero=int(input("Ingrese un número: "))
    lista.append(numero)

print("Los números en orden inverso son: ")
for numero in reversed(lista):
    print(numero)
    
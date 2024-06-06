lista=[]
eliminar="aA"

for n in range(7):
    palabra=input("Ingrese un nombre: ")
    lista.append(palabra)

eliminarlis=lista.copy()
for palabra in eliminarlis:
    for letra in palabra: 
        letra=palabra[-1]
        if letra in eliminar:
            palabra=eliminarlis.pop()
print(eliminarlis)
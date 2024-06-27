lista=[]
suma_notas=0
contador=0
print("Ingrese las notas que quiera: ")
while True:
    notas=float(input())
    lista.append(notas)
    if notas==0:
        break
    suma_notas=suma_notas + notas
    contador=contador+1

promedio=suma_notas/contador
mayor=lista.copy()
mayor.sort(reverse=True)
menor=lista.copy()
menor.sort()

print("La cantidad de notas es: " + str(len(lista)))
print("El promedio de las notas es: " + str(promedio))
print("La nota más baja fue: " + str(menor[1]))
print("La nota máxima fue: " + str(mayor[0]))



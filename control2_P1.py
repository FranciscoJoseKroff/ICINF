lista=[]
menor_70=0
mayor_o_igual70=0
while True:
    puntaje=int(input("Ingrese el puntaje del alumno:"))
    lista.append(puntaje)
    if (puntaje > 100) or (puntaje < 1):
        print("Puntaje no válido, por favor ingrese un numero del 1 al 100")
    else:
        break
for n in range(15):
    print("Día", n)
    puntaje=int(input("Ingrese el puntaje del alumno:"))
    lista.append(puntaje)
    if  1 < puntaje < 70:
        menor_70 +=1
    if  puntaje >= 70:
        mayor_o_igual70+=1

lista_ascendente=lista.copy()
lista_ascendente.sort()
print(lista_ascendente, n)
            
    


lista=[]

while True:
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista según el índice")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")
    opcion=input("Seleccione una opción (1-7): ")
    if opcion=="1":
        elemento=input("Introduzca el elemento a añadir: ")
        lista.append(elemento)
        print("Elemento añadido a la lista.")
    elif opcion=="2":
        indice=int(input("Ingrese el indice que desea cambiar."))
        if 0<= indice < len(lista):
            nuevo_elemento=input("Ingrese el valor del nuevo elemento.")
            lista[indice] = nuevo_elemento
            print("Elemento modificado.")
        else:
            print("Índice no válido.")
    elif opcion=="3":
        indice=int(input("Ingrese el indice a eliminar."))
        if 0<= indice < len(lista):
            eliminado=lista.pop(indice)
            print("El elemento:", eliminado, "eliminado de la lista.")
        else:
            print("Índice no válido")
    elif opcion=="4":
        if lista:
            eliminado=lista.pop()
            print("Último elemento:", eliminado, "eliminado de la lista.")
        else:
            print("La lista está vacía.")
    elif opcion=="5":
        elemento=input("Ingrese el elemento a buscar en la lista: ")
        if elemento in lista:
            indice = lista.index(elemento)
            print("Elemento encontrado en el índice", indice)
        else:
            print("Elemento no encontrado en la lista.")
    elif opcion=="6":
        if lista:
            print(lista)
        else:
            print("La lista está vacía.")
    elif opcion=="7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del (1 al 7)")